# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lapse_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_lapse_window(object):
    def setupUi(self, lapse_window):
        if not lapse_window.objectName():
            lapse_window.setObjectName(u"lapse_window")
        lapse_window.resize(800, 600)
        self.centralwidget = QWidget(lapse_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.images_fld = QLineEdit(self.centralwidget)
        self.images_fld.setObjectName(u"images_fld")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.images_fld)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.interval_fld = QLineEdit(self.centralwidget)
        self.interval_fld.setObjectName(u"interval_fld")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.interval_fld)

        self.images_btn = QPushButton(self.centralwidget)
        self.images_btn.setObjectName(u"images_btn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.images_btn)

        self.time_fld = QDateTimeEdit(self.centralwidget)
        self.time_fld.setObjectName(u"time_fld")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.time_fld)

        self.saveas_btn = QPushButton(self.centralwidget)
        self.saveas_btn.setObjectName(u"saveas_btn")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.saveas_btn)

        self.saveas_fld = QLineEdit(self.centralwidget)
        self.saveas_fld.setObjectName(u"saveas_fld")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.saveas_fld)

        self.make_timelapse_btn = QPushButton(self.centralwidget)
        self.make_timelapse_btn.setObjectName(u"make_timelapse_btn")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.make_timelapse_btn)


        self.verticalLayout.addLayout(self.formLayout)

        lapse_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(lapse_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        lapse_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(lapse_window)
        self.statusbar.setObjectName(u"statusbar")
        lapse_window.setStatusBar(self.statusbar)

        self.retranslateUi(lapse_window)

        QMetaObject.connectSlotsByName(lapse_window)
    # setupUi

    def retranslateUi(self, lapse_window):
        lapse_window.setWindowTitle(QCoreApplication.translate("lapse_window", u"lapse_window", None))
        self.label_2.setText(QCoreApplication.translate("lapse_window", u"Start Time", None))
        self.label_3.setText(QCoreApplication.translate("lapse_window", u"Interval (s)", None))
        self.interval_fld.setText(QCoreApplication.translate("lapse_window", u"0", None))
        self.images_btn.setText(QCoreApplication.translate("lapse_window", u"Images", None))
        self.time_fld.setDisplayFormat(QCoreApplication.translate("lapse_window", u"yyyy-MM-dd h:mm", None))
        self.saveas_btn.setText(QCoreApplication.translate("lapse_window", u"Save As", None))
        self.make_timelapse_btn.setText(QCoreApplication.translate("lapse_window", u"Make Timelapse", None))
    # retranslateUi

