#ifndef LAPSE_WINDOW_H
#define LAPSE_WINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class lapse_window; }
QT_END_NAMESPACE

class lapse_window : public QMainWindow
{
    Q_OBJECT

public:
    lapse_window(QWidget *parent = nullptr);
    ~lapse_window();

private:
    Ui::lapse_window *ui;
};
#endif // LAPSE_WINDOW_H
