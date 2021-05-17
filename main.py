# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui',
# licensing of 'main.ui' applies.
#
# Created: Mon May 17 17:35:08 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

import res_1
from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 752)
        MainWindow.setStyleSheet("QToolTip\n"
                                 "{\n"
                                 "     border: 1px solid black;\n"
                                 "     background-color: #ffa02f;\n"
                                 "     padding: 1px;\n"
                                 "     border-radius: 3px;\n"
                                 "     opacity: 100;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "}\n"
                                 "\n"
                                 "QTreeView, QListView\n"
                                 "{\n"
                                 "    background-color: silver;\n"
                                 "    margin-left: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:hover\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
                                 "    color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:item:selected\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:selected\n"
                                 "{\n"
                                 "    background: transparent;\n"
                                 "    border: 1px solid #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QMenuBar::item:pressed\n"
                                 "{\n"
                                 "    background: #444;\n"
                                 "    border: 1px solid #000;\n"
                                 "    background-color: QLinearGradient(\n"
                                 "        x1:0, y1:0,\n"
                                 "        x2:0, y2:1,\n"
                                 "        stop:1 #212121,\n"
                                 "        stop:0.4 #343434/*,\n"
                                 "        stop:0.2 #343434,\n"
                                 "        stop:0.1 #ffaa00*/\n"
                                 "    );\n"
                                 "    margin-bottom:-1px;\n"
                                 "    padding-bottom:1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu\n"
                                 "{\n"
                                 "    border: 1px solid #000;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item\n"
                                 "{\n"
                                 "    padding: 2px 20px 2px 20px;\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::item:selected\n"
                                 "{\n"
                                 "    color: #000000;\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:disabled\n"
                                 "{\n"
                                 "    color: #808080;\n"
                                 "    background-color: #323232;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractItemView\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
                                 "}\n"
                                 "\n"
                                 "QWidget:focus\n"
                                 "{\n"
                                 "    /*border: 1px solid darkgray;*/\n"
                                 "}\n"
                                 "\n"
                                 "QLineEdit\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
                                 "    padding: 1px;\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-width: 1px;\n"
                                 "    border-color: #1e1e1e;\n"
                                 "    border-style: solid;\n"
                                 "    border-radius: 6;\n"
                                 "    padding: 3px;\n"
                                 "    font-size: 12px;\n"
                                 "    padding-left: 5px;\n"
                                 "    padding-right: 5px;\n"
                                 "    min-width: 40px;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:pressed\n"
                                 "{\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox\n"
                                 "{\n"
                                 "    selection-background-color: #ffaa00;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
                                 "    border-style: solid;\n"
                                 "    border: 1px solid #1e1e1e;\n"
                                 "    border-radius: 5;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox:hover,QPushButton:hover\n"
                                 "{\n"
                                 "    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QComboBox:on\n"
                                 "{\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-left: 4px;\n"
                                 "    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
                                 "    selection-background-color: #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox QAbstractItemView\n"
                                 "{\n"
                                 "    border: 2px solid darkgray;\n"
                                 "    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox::drop-down\n"
                                 "{\n"
                                 "     subcontrol-origin: padding;\n"
                                 "     subcontrol-position: top right;\n"
                                 "     width: 15px;\n"
                                 "\n"
                                 "     border-left-width: 0px;\n"
                                 "     border-left-color: darkgray;\n"
                                 "     border-left-style: solid; /* just a single line */\n"
                                 "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                 "     border-bottom-right-radius: 3px;\n"
                                 " }\n"
                                 "\n"
                                 "QComboBox::down-arrow\n"
                                 "{\n"
                                 "     image: url(:/dark_orange/img/down_arrow.png);\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox\n"
                                 "{\n"
                                 "    border: 1px solid darkgray;\n"
                                 "    margin-top: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "QGroupBox:focus\n"
                                 "{\n"
                                 "    border: 1px solid darkgray;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit:focus\n"
                                 "{\n"
                                 "    border: 1px solid darkgray;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:horizontal {\n"
                                 "     border: 1px solid #222222;\n"
                                 "     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                 "     height: 7px;\n"
                                 "     margin: 0px 16px 0 16px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:horizontal\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                 "      min-height: 20px;\n"
                                 "      border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:horizontal {\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "      width: 14px;\n"
                                 "      subcontrol-position: right;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:horizontal {\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "      width: 14px;\n"
                                 "     subcontrol-position: left;\n"
                                 "     subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
                                 "{\n"
                                 "      border: 1px solid black;\n"
                                 "      width: 1px;\n"
                                 "      height: 1px;\n"
                                 "      background: white;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
                                 "{\n"
                                 "      background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar:vertical\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
                                 "      width: 7px;\n"
                                 "      margin: 16px 0 16px 0;\n"
                                 "      border: 1px solid #222222;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::handle:vertical\n"
                                 "{\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
                                 "      min-height: 20px;\n"
                                 "      border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::add-line:vertical\n"
                                 "{\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
                                 "      height: 14px;\n"
                                 "      subcontrol-position: bottom;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::sub-line:vertical\n"
                                 "{\n"
                                 "      border: 1px solid #1b1b19;\n"
                                 "      border-radius: 2px;\n"
                                 "      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
                                 "      height: 14px;\n"
                                 "      subcontrol-position: top;\n"
                                 "      subcontrol-origin: margin;\n"
                                 "}\n"
                                 "\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
                                 "{\n"
                                 "      border: 1px solid black;\n"
                                 "      width: 1px;\n"
                                 "      height: 1px;\n"
                                 "      background: white;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
                                 "{\n"
                                 "      background: none;\n"
                                 "}\n"
                                 "\n"
                                 "QTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QPlainTextEdit\n"
                                 "{\n"
                                 "    background-color: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section\n"
                                 "{\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox:disabled\n"
                                 "{\n"
                                 "color: #414141;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::title\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button, QDockWidget::float-button\n"
                                 "{\n"
                                 "    text-align: center;\n"
                                 "    spacing: 1px; /* spacing between items in the tool bar */\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
                                 "{\n"
                                 "    background: #242424;\n"
                                 "}\n"
                                 "\n"
                                 "QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
                                 "{\n"
                                 "    padding: 1px -1px -1px 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator\n"
                                 "{\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #4c4c4c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QMainWindow::separator:hover\n"
                                 "{\n"
                                 "\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    border: 1px solid #6c6c6c;\n"
                                 "    spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "}\n"
                                 "\n"
                                 "QToolBar::handle\n"
                                 "{\n"
                                 "     spacing: 3px; /* spacing between items in the tool bar */\n"
                                 "     background: url(:/dark_orange/img/handle.png);\n"
                                 "}\n"
                                 "\n"
                                 "QMenu::separator\n"
                                 "{\n"
                                 "    height: 2px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
                                 "    color: white;\n"
                                 "    padding-left: 4px;\n"
                                 "    margin-left: 10px;\n"
                                 "    margin-right: 5px;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar\n"
                                 "{\n"
                                 "    border: 2px solid grey;\n"
                                 "    border-radius: 5px;\n"
                                 "    text-align: center;\n"
                                 "}\n"
                                 "\n"
                                 "QProgressBar::chunk\n"
                                 "{\n"
                                 "    background-color: #d7801a;\n"
                                 "    width: 2.15px;\n"
                                 "    margin: 0.5px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab {\n"
                                 "    color: #b1b1b1;\n"
                                 "    border: 1px solid #444;\n"
                                 "    border-bottom-style: none;\n"
                                 "    background-color: #323232;\n"
                                 "    padding-left: 10px;\n"
                                 "    padding-right: 10px;\n"
                                 "    padding-top: 3px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    margin-right: -1px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::pane {\n"
                                 "    border: 1px solid #444;\n"
                                 "    top: 1px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:last\n"
                                 "{\n"
                                 "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:first:!selected\n"
                                 "{\n"
                                 " margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "\n"
                                 "\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:!selected\n"
                                 "{\n"
                                 "    color: #b1b1b1;\n"
                                 "    border-bottom-style: solid;\n"
                                 "    margin-top: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected\n"
                                 "{\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    margin-bottom: 0px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:!selected:hover\n"
                                 "{\n"
                                 "    /*border-top: 2px solid #ffaa00;\n"
                                 "    padding-bottom: 3px;*/\n"
                                 "    border-top-left-radius: 3px;\n"
                                 "    border-top-right-radius: 3px;\n"
                                 "    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:checked\n"
                                 "{\n"
                                 "    background-color: qradialgradient(\n"
                                 "        cx: 0.5, cy: 0.5,\n"
                                 "        fx: 0.5, fy: 0.5,\n"
                                 "        radius: 1.0,\n"
                                 "        stop: 0.25 #ffaa00,\n"
                                 "        stop: 0.3 #323232\n"
                                 "    );\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator{\n"
                                 "    color: #b1b1b1;\n"
                                 "    background-color: #323232;\n"
                                 "    border: 1px solid #b1b1b1;\n"
                                 "    width: 9px;\n"
                                 "    height: 9px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator\n"
                                 "{\n"
                                 "    border-radius: 6px;\n"
                                 "}\n"
                                 "\n"
                                 "QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
                                 "{\n"
                                 "    border: 1px solid #ffaa00;\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:checked\n"
                                 "{\n"
                                 "    image:url(:/dark_orange/img/checkbox.png);\n"
                                 "}\n"
                                 "\n"
                                 "QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
                                 "{\n"
                                 "    border: 1px solid #444;\n"
                                 "}\n"
                                 "\n"
                                 "\n"
                                 "QSlider::groove:horizontal {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    height: 8px;\n"
                                 "    background: #201F1F;\n"
                                 "    margin: 2px 0;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:horizontal {\n"
                                 "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
                                 "      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 14px;\n"
                                 "    height: 14px;\n"
                                 "    margin: -4px 0;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::groove:vertical {\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 8px;\n"
                                 "    background: #201F1F;\n"
                                 "    margin: 0 0px;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QSlider::handle:vertical {\n"
                                 "    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,\n"
                                 "      stop: 0.2 #a8a8a8, stop: 1 #727272);\n"
                                 "    border: 1px solid #3A3939;\n"
                                 "    width: 14px;\n"
                                 "    height: 14px;\n"
                                 "    margin: 0 -4px;\n"
                                 "    border-radius: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QAbstractSpinBox {\n"
                                 "    padding-top: 2px;\n"
                                 "    padding-bottom: 2px;\n"
                                 "    border: 1px solid darkgray;\n"
                                 "\n"
                                 "    border-radius: 2px;\n"
                                 "    min-width: 50px;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("font: 75 30pt \"Century Gothic\";\n"
                                 "background-color: rgb(170, 170, 170);\n"
                                 "color: rgb(74, 105, 204);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.count_filter_txt = QtWidgets.QSpinBox(self.frame_2)
        self.count_filter_txt.setObjectName("count_filter_txt")
        self.gridLayout_4.addWidget(self.count_filter_txt, 0, 1, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.frame_2)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_4.addWidget(self.search_btn, 0, 2, 1, 1)
        self.table = QtWidgets.QTableWidget(self.frame_2)
        self.table.setStyleSheet("font: 10pt \"Century Gothic\";")
        self.table.setObjectName("table")
        self.table.setColumnCount(9)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        self.gridLayout_4.addWidget(self.table, 1, 0, 1, 3)
        self.gridLayout_3.addWidget(self.frame_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 0, 1, 1)
        self.lbl_ref_nbr = QtWidgets.QLabel(self.frame_3)
        self.lbl_ref_nbr.setStyleSheet("font: 24pt \"Century Gothic\";\n"
                                       "color: rgb(100, 100, 255)\n"
                                       "")
        self.lbl_ref_nbr.setObjectName("lbl_ref_nbr")
        self.gridLayout_6.addWidget(self.lbl_ref_nbr, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 0, 2, 1, 1)
        self.lbl_min_holes = QtWidgets.QLabel(self.frame_3)
        self.lbl_min_holes.setStyleSheet("font: 24pt \"Century Gothic\";\n"
                                         "color: rgb(100, 100, 255)\n"
                                         "")
        self.lbl_min_holes.setObjectName("lbl_min_holes")
        self.gridLayout_6.addWidget(self.lbl_min_holes, 0, 3, 1, 2)
        self.lbl_min_holes2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_min_holes2.setStyleSheet("font: 24pt \"Century Gothic\";\n"
                                          "color: rgb(100, 100, 255)\n"
                                          "")
        self.lbl_min_holes2.setObjectName("lbl_min_holes2")
        self.gridLayout_6.addWidget(self.lbl_min_holes2, 0, 6, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_6.addWidget(self.label_4, 1, 0, 1, 1)
        self.lbl_parts_nbr = QtWidgets.QLabel(self.frame_3)
        self.lbl_parts_nbr.setStyleSheet("font: 24pt \"Century Gothic\";\n"
                                         "color: rgb(100, 100, 255)\n"
                                         "")
        self.lbl_parts_nbr.setObjectName("lbl_parts_nbr")
        self.gridLayout_6.addWidget(self.lbl_parts_nbr, 1, 1, 1, 1)
        self.lbl_max_holes = QtWidgets.QLabel(self.frame_3)
        self.lbl_max_holes.setStyleSheet("font: 24pt \"Century Gothic\";\n"
                                         "color: rgb(100, 100, 255)\n"
                                         "")
        self.lbl_max_holes.setObjectName("lbl_max_holes")
        self.gridLayout_6.addWidget(self.lbl_max_holes, 1, 4, 1, 1)
        self.lbl_max_holes2 = QtWidgets.QLabel(self.frame_3)
        self.lbl_max_holes2.setStyleSheet("font: 24pt \"Century Gothic\";\n"
                                          "color: rgb(100, 100, 255)\n"
                                          "")
        self.lbl_max_holes2.setObjectName("lbl_max_holes2")
        self.gridLayout_6.addWidget(self.lbl_max_holes2, 1, 6, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 2, 0, 1, 3)
        self.table2 = QtWidgets.QTableWidget(self.frame_3)
        self.table2.setStyleSheet("font: 11pt \"Century Gothic\";")
        self.table2.setObjectName("table2")
        self.table2.setColumnCount(3)
        self.table2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table2.setHorizontalHeaderItem(2, item)
        self.gridLayout_6.addWidget(self.table2, 3, 0, 1, 2)
        self.check_btn = QtWidgets.QPushButton(self.frame_3)
        self.check_btn.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.check_btn.setObjectName("check_btn")
        self.gridLayout_6.addWidget(self.check_btn, 3, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 2, 1, 2)
        self.gridLayout_5.addWidget(self.frame_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.add_btn = QtWidgets.QPushButton(self.frame_4)
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_8.addWidget(self.add_btn, 6, 8, 1, 1)
        self.part_name = QtWidgets.QLineEdit(self.frame_4)
        self.part_name.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                     "color: rgb(255, 0, 255)")
        self.part_name.setText("")
        self.part_name.setObjectName("part_name")
        self.gridLayout_8.addWidget(self.part_name, 3, 2, 1, 1)
        self.count = QtWidgets.QSpinBox(self.frame_4)
        self.count.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                 "color: rgb(255, 0, 255)")
        self.count.setObjectName("count")
        self.gridLayout_8.addWidget(self.count, 5, 7, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setObjectName("label_7")
        self.gridLayout_8.addWidget(self.label_7, 4, 5, 1, 1)
        self.last_btn = QtWidgets.QPushButton(self.frame_4)
        self.last_btn.setStyleSheet("font: 18pt \"Century Gothic\";\n"
                                    "color: rgb(100, 100, 255)")
        self.last_btn.setObjectName("last_btn")
        self.gridLayout_8.addWidget(self.last_btn, 6, 4, 1, 1)
        self.first_btn = QtWidgets.QPushButton(self.frame_4)
        self.first_btn.setStyleSheet("font: 18pt \"Century Gothic\";\n"
                                     "color: rgb(100, 100, 255)")
        self.first_btn.setObjectName("first_btn")
        self.gridLayout_8.addWidget(self.first_btn, 6, 0, 1, 1)
        self.max_area = QtWidgets.QLineEdit(self.frame_4)
        self.max_area.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                    "color: rgb(255, 0, 255)")
        self.max_area.setText("")
        self.max_area.setObjectName("max_area")
        self.gridLayout_8.addWidget(self.max_area, 5, 2, 1, 1)
        self.number_of_holes = QtWidgets.QLineEdit(self.frame_4)
        self.number_of_holes.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                           "color: rgb(255, 0, 255)")
        self.number_of_holes.setText("")
        self.number_of_holes.setObjectName("number_of_holes")
        self.gridLayout_8.addWidget(self.number_of_holes, 2, 7, 1, 2)
        self.previous_btn = QtWidgets.QPushButton(self.frame_4)
        self.previous_btn.setStyleSheet("font: 18pt \"Century Gothic\";\n"
                                        "color: rgb(100, 100, 255)")
        self.previous_btn.setObjectName("previous_btn")
        self.gridLayout_8.addWidget(self.previous_btn, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 2, 5, 1, 2)
        self.min_area = QtWidgets.QLineEdit(self.frame_4)
        self.min_area.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                    "color: rgb(255, 0, 255)")
        self.min_area.setText("")
        self.min_area.setObjectName("min_area")
        self.gridLayout_8.addWidget(self.min_area, 4, 2, 1, 1)
        self.next_btn = QtWidgets.QPushButton(self.frame_4)
        self.next_btn.setStyleSheet("font: 18pt \"Century Gothic\";\n"
                                    "color: rgb(100, 100, 255)")
        self.next_btn.setObjectName("next_btn")
        self.gridLayout_8.addWidget(self.next_btn, 6, 3, 1, 1)
        self.max_diameter = QtWidgets.QLineEdit(self.frame_4)
        self.max_diameter.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                        "color: rgb(255, 0, 255)")
        self.max_diameter.setText("")
        self.max_diameter.setObjectName("max_diameter")
        self.gridLayout_8.addWidget(self.max_diameter, 4, 7, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_8.addWidget(self.label_9, 3, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_8.addWidget(self.label_16, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_8.addWidget(self.label_12, 5, 5, 1, 1)
        self.reference = QtWidgets.QLineEdit(self.frame_4)
        self.reference.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                     "color: rgb(255, 0, 255)")
        self.reference.setText("")
        self.reference.setObjectName("reference")
        self.gridLayout_8.addWidget(self.reference, 2, 2, 1, 1)
        self.min_diameter = QtWidgets.QLineEdit(self.frame_4)
        self.min_diameter.setStyleSheet("font: 14pt \"Century Gothic\";\n"
                                        "color: rgb(255, 0, 255)")
        self.min_diameter.setText("")
        self.min_diameter.setObjectName("min_diameter")
        self.gridLayout_8.addWidget(self.min_diameter, 3, 7, 1, 2)
        self.delete_btn = QtWidgets.QPushButton(self.frame_4)
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout_8.addWidget(self.delete_btn, 6, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_8.addWidget(self.label_11, 4, 0, 1, 1)
        self.update_btn = QtWidgets.QPushButton(self.frame_4)
        self.update_btn.setObjectName("update_btn")
        self.gridLayout_8.addWidget(self.update_btn, 6, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)
        self.id = QtWidgets.QLabel(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                              "font: 75 12pt \"Century Gothic\";\n"
                              "color: rgb(255, 0, 255)")
        self.id.setText("")
        self.id.setObjectName("id")
        self.gridLayout_8.addWidget(self.id, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 3)
        self.refresh_btn = QtWidgets.QPushButton(self.frame)
        self.refresh_btn.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.refresh_btn.setObjectName("refresh_btn")
        self.gridLayout_2.addWidget(self.refresh_btn, 2, 0, 1, 1)
        self.theme1_btn = QtWidgets.QPushButton(self.frame)
        self.theme1_btn.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.theme1_btn.setObjectName("theme1_btn")
        self.gridLayout_2.addWidget(self.theme1_btn, 2, 1, 1, 1)
        self.theme2_btn = QtWidgets.QPushButton(self.frame)
        self.theme2_btn.setStyleSheet("font: 16pt \"Century Gothic\";")
        self.theme2_btn.setObjectName("theme2_btn")
        self.gridLayout_2.addWidget(self.theme2_btn, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate(
            "MainWindow", "Parts Inventory Manager", None, -1))
        self.label.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Parts Inventory Manager", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Search of references with count level lower or equal to:", None, -1))
        self.search_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Search", None, -1))
        self.table.horizontalHeaderItem(0).setText(
            QtWidgets.QApplication.translate("MainWindow", "ID", None, -1))
        self.table.horizontalHeaderItem(1).setText(
            QtWidgets.QApplication.translate("MainWindow", "Reference", None, -1))
        self.table.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("MainWindow", "PartName", None, -1))
        self.table.horizontalHeaderItem(3).setText(
            QtWidgets.QApplication.translate("MainWindow", "MinArea", None, -1))
        self.table.horizontalHeaderItem(4).setText(
            QtWidgets.QApplication.translate("MainWindow", "MaxArea", None, -1))
        self.table.horizontalHeaderItem(5).setText(
            QtWidgets.QApplication.translate("MainWindow", "NumberOfHoles", None, -1))
        self.table.horizontalHeaderItem(6).setText(
            QtWidgets.QApplication.translate("MainWindow", "MinDiameter", None, -1))
        self.table.horizontalHeaderItem(7).setText(
            QtWidgets.QApplication.translate("MainWindow", "MaxDiameter", None, -1))
        self.table.horizontalHeaderItem(8).setText(
            QtWidgets.QApplication.translate("MainWindow", "Count", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), QtWidgets.QApplication.translate("MainWindow", "Inventory Details", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Number of Reference", None, -1))
        self.lbl_ref_nbr.setText(
            QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Min. Number of Holes", None, -1))
        self.lbl_min_holes.setText(
            QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.lbl_min_holes2.setText(
            QtWidgets.QApplication.translate("MainWindow", "REF", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Number of parts type", None, -1))
        self.lbl_parts_nbr.setText(
            QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.lbl_max_holes.setText(
            QtWidgets.QApplication.translate("MainWindow", "0", None, -1))
        self.lbl_max_holes2.setText(
            QtWidgets.QApplication.translate("MainWindow", "REF", None, -1))
        self.label_13.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Top 3 Reference with minimum inventory level", None, -1))
        self.table2.horizontalHeaderItem(0).setText(
            QtWidgets.QApplication.translate("MainWindow", "Reference", None, -1))
        self.table2.horizontalHeaderItem(1).setText(
            QtWidgets.QApplication.translate("MainWindow", "Part Name", None, -1))
        self.table2.horizontalHeaderItem(2).setText(
            QtWidgets.QApplication.translate("MainWindow", "Count", None, -1))
        self.check_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Check", None, -1))
        self.label_8.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Max. Number of Holes", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtWidgets.QApplication.translate(
            "MainWindow", "Inventory Statistics", None, -1))
        self.add_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Add", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Max Diameter", None, -1))
        self.last_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", ">>", None, -1))
        self.first_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "<<", None, -1))
        self.previous_btn.setText(
            QtWidgets.QApplication.translate("MainWindow", "<", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Number of Holes", None, -1))
        self.next_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", ">", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Min Diameter", None, -1))
        self.label_15.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Max Area", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Reference", None, -1))
        self.label_16.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Part Name", None, -1))
        self.label_12.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Count", None, -1))
        self.delete_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Delete", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Min Area", None, -1))
        self.update_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Update", None, -1))
        self.label_14.setText(QtWidgets.QApplication.translate(
            "MainWindow", "ID", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), QtWidgets.QApplication.translate("MainWindow", "Edit Inventory", None, -1))
        self.refresh_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Refresh", None, -1))
        self.theme1_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Theme 1", None, -1))
        self.theme2_btn.setText(QtWidgets.QApplication.translate(
            "MainWindow", "Theme 2", None, -1))
