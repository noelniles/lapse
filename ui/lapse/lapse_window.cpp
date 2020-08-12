#include "lapse_window.h"
#include "ui_lapse_window.h"

lapse_window::lapse_window(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::lapse_window)
{
    ui->setupUi(this);
}

lapse_window::~lapse_window()
{
    delete ui;
}

