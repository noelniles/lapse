import sys
from datetime import timedelta
from pathlib import Path

from PySide2.QtWidgets import QApplication, QFileDialog, QMainWindow
from PySide2.QtCore import QThreadPool
from skvideo.io import FFmpegWriter
from skimage import io

from imutils import annotate_image
from fsutils import list_images
from lapse_window import Ui_lapse_window
from runnable import Worker


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_lapse_window()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()

        self.start_time       = self.ui.time_fld.dateTime().toPython()
        self.current_time     = self.start_time
        self.images_directory = None
        self.saveas           = None
        self.interval         = int(self.ui.interval_fld.text())
        self.files            = []
        self.nfiles           = lambda: len(self.files)

        self.fps      = 60
        self.imwidth  = 0
        self.imheight = 0
        self.crf      = 17

        self.connect()

    def connect(self):
        self.ui.images_fld.editingFinished.connect(self.on_images_changed)
        self.ui.images_btn.clicked.connect(self.on_images_btn)
        self.ui.saveas_fld.editingFinished.connect(self.on_saveas_changed)
        self.ui.saveas_btn.clicked.connect(self.on_saveas_btn)
        self.ui.time_fld.dateChanged.connect(self.on_time_change)
        self.ui.interval_fld.editingFinished.connect(self.on_interval_change)
        self.ui.make_timelapse_btn.clicked.connect(self.run)

    def on_images_btn(self):
        path = QFileDialog.getExistingDirectory()
        self.ui.images_fld.setText(path)
        self.images_directory = Path(path)
        self.files = list_images(self.images_directory)

        tmp = io.imread(self.files[0])
        self.imwidth, self.imheight, _ = tmp.shape

    def on_images_changed(self):
        path = Path(self.ui.images_fld.text())

        if not path.exists():
            self.images_directory = None
            return
        self.files = list_images(self.images_directory)
        
    def on_saveas_btn(self):
        fn = QFileDialog.getSaveFileName(self, "Save", "untitled.mp4",
                                         "Video (*.mp4)")[0]
        self.ui.saveas_fld.setText(fn)
        self.saveas = Path(fn)

    def on_saveas_changed(self):
        self.saveas = Path(self.ui.saveas_fld.text())

    def on_time_change(self):
        tm = self.ui.time_fld.dateTime()
        self.start_time = tm.toPython()
        self.current_time = self.start_time

    def on_interval_change(self):
        self.interval = int(self.ui.interval_fld.text())

    def run_threaded_process(self, process, progress_fn, on_complete):
        """Execute a function in the background with a worker"""
        worker = Worker(fn=process)
        self.threadpool.start(worker)
        worker.signals.finished.connect(on_complete)
        worker.signals.progress.connect(progress_fn)

    def progress_fn(self, msg):
        self.ui.statusbar.showMessage(str(msg))

    def completed(self):
        self.ui.statusbar.showMessage(f'Finished making {self.saveas}')

    def run(self):
        self.run_threaded_process(self.make_timelapse, self.progress_fn, self.completed)

    def validate_form(self):
        reasons = []
        valid = False
        if self.nfiles() == 0:
            self.ui.images_btn.setStyleSheet('background-color: red;')
            reasons.append('no image files')
        else:
            self.ui.images_btn.setStyleSheet('background-color: green;')
            valid = True
        if self.saveas is None or self.saveas == '':
            self.ui.saveas_btn.setStyleSheet('background-color: red;')
            reasons.append('save as field is empty')
        else:
            self.ui.saveas_btn.setStyleSheet('background-color: green;')
            valid = True
        if self.imwidth == 0 or self.imheight == 0:
            reasons.append(f'{self.imwidth}x{self.imheight} are not valid dimensions')
            valid = False

        self.on_time_change()
        
        reason = '\n'.join(reasons)
        return reason, valid

    def make_timelapse(self, progress_callback):
        reason, valid = self.validate_form()
        if not valid:
            self.ui.statusbar.showMessage(reason)
            return
        video = FFmpegWriter(self.saveas,
                            inputdict={
                                '-r': str(self.fps)},
                            outputdict={
                                '-r': str(self.fps),
                                '-c:v': 'libx264',
                                '-crf': str(self.crf),
                                '-preset': 'ultrafast',
                                '-pix_fmt': 'yuv444p'})

        for i, f in enumerate(self.files):
            msg = f'processing {i}/{self.nfiles()}'
            progress_callback.emit(msg)
            try:
                im = io.imread(f)
            except:
                continue

            dt = self.current_time + timedelta(seconds=self.interval)
            self.current_time = dt
            annotation = dt.isoformat()
            im = annotate_image(im, annotation, (16, 16))
            try:
                video.writeFrame(im)
            except ValueError:
                w, h, _ = im.shape
                print(f'{f} is {w}x{h} when it should be {self.imwidth}x{self.imheight}')
                continue
                
        video.close()

if __name__ == '__main__':
    app = QApplication([])       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.resize(640, 520)
    window.show()
    exit_code = app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)