classic = """ QWidget {
    font-size: 11px;
}

QTableView {
    font-size: 10px;
    alternate-background-color: #EEEEFF;
}

Browser QPushButton {
    font-size: 10px;
    min-width: 10px;
}

ColorButton::enabled {
    border: 1px solid #444444;
}

ColorButton::disabled {
    border: 1px solid #AAAAAA;
}


Browser QGroupBox {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 #E0E0E0, stop: 1 #FFFFFF);
    border: 2px solid #999999;
    border-radius: 5px;
    margin-top: 1ex; /* leave space at the top for the title */
    font-size: 13px;
    color: black;
}

Browser QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center; /* position at the top center */
    padding: 0 3px;
    font-size: 13px;
    color: black;
}

PluginItem {
    border: 2px solid black;
    background: white;
}


PluginItem Frame {
    background: #CCCCCC;
}


TabButton {
    border: 1px solid #8f8f91;
    border-radius: 2px;
    padding: 3px;
    min-width: 120px;
}

TabButton::checked {
    background-color: qlineargradient(x1: 0, y1: 0 , x2: 0, y2: 1,
                                      stop: 0 #9a9b9e, stop: 1 #babbbe);
}


TabButton::pressed {
    background-color: qlineargradient(x1: 0, y1: 0 , x2: 0, y2: 1,
                                      stop: 0 #9a9b9e, stop: 1 #babbbe);
} """
# ----------------------------------------------------------------------------------------
darkBlue = """ QProgressBar:horizontal {
    border: 1px solid #3A3939;
    text-align: center;
    padding: 1px;
    background: #201F1F;
}
QProgressBar::chunk:horizontal {
    background-color: qlineargradient(spread:reflect, x1:1, y1:0.545, x2:1, y2:0, stop:0 rgba(28, 66, 111, 255), stop:1 rgba(37, 87, 146, 255));
}

QToolTip
{
    border: 1px solid #3A3939;
    background-color: rgb(90, 102, 117);;
    color: white;
    padding: 1px;
    opacity: 200;
}

QWidget
{
    color: silver;
    background-color: #302F2F;
    selection-background-color:#3d8ec9;
    selection-color: black;
    background-clip: border;
    border-image: none;
    outline: 0;
}

QWidget:item:hover
{
    background-color: #78879b;
    color: black;
}

QWidget:item:selected
{
    background-color: #3d8ec9;
}

QCheckBox
{
    spacing: 5px;
    outline: none;
    color: #bbb;
    margin-bottom: 2px;
}

QCheckBox:disabled
{
    color: #777777;
}
QCheckBox::indicator,
QGroupBox::indicator
{
    width: 18px;
    height: 18px;
}
QGroupBox::indicator
{
    margin-left: 2px;
}

QCheckBox::indicator:unchecked,
QCheckBox::indicator:unchecked:hover,
QGroupBox::indicator:unchecked,
QGroupBox::indicator:unchecked:hover
{
    image: url(:/dark_blue/img/checkbox_unchecked.png);
}

QCheckBox::indicator:unchecked:focus,
QCheckBox::indicator:unchecked:pressed,
QGroupBox::indicator:unchecked:focus,
QGroupBox::indicator:unchecked:pressed
{
  border: none;
    image: url(:/dark_blue/img/checkbox_unchecked_focus.png);
}

QCheckBox::indicator:checked,
QCheckBox::indicator:checked:hover,
QGroupBox::indicator:checked,
QGroupBox::indicator:checked:hover
{
    image: url(:/dark_blue/img/checkbox_checked.png);
}

QCheckBox::indicator:checked:focus,
QCheckBox::indicator:checked:pressed,
QGroupBox::indicator:checked:focus,
QGroupBox::indicator:checked:pressed
{
  border: none;
    image: url(:/dark_blue/img/checkbox_checked_focus.png);
}

QCheckBox::indicator:indeterminate,
QCheckBox::indicator:indeterminate:hover,
QCheckBox::indicator:indeterminate:pressed
QGroupBox::indicator:indeterminate,
QGroupBox::indicator:indeterminate:hover,
QGroupBox::indicator:indeterminate:pressed
{
    image: url(:/dark_blue/img/checkbox_indeterminate.png);
}

QCheckBox::indicator:indeterminate:focus,
QGroupBox::indicator:indeterminate:focus
{
    image: url(:/dark_blue/img/checkbox_indeterminate_focus.png);
}

QCheckBox::indicator:checked:disabled,
QGroupBox::indicator:checked:disabled
{
    image: url(:/dark_blue/img/checkbox_checked_disabled.png);
}

QCheckBox::indicator:unchecked:disabled,
QGroupBox::indicator:unchecked:disabled
{
    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);
}

QRadioButton
{
    spacing: 5px;
    outline: none;
    color: #bbb;
    margin-bottom: 2px;
}

QRadioButton:disabled
{
    color: #777777;
}
QRadioButton::indicator
{
    width: 21px;
    height: 21px;
}

QRadioButton::indicator:unchecked,
QRadioButton::indicator:unchecked:hover
{
    image: url(:/dark_blue/img/radio_unchecked.png);
}

QRadioButton::indicator:unchecked:focus,
QRadioButton::indicator:unchecked:pressed
{
  border: none;
  outline: none;
    image: url(:/dark_blue/img/radio_unchecked_focus.png);
}

QRadioButton::indicator:checked,
QRadioButton::indicator:checked:hover
{
  border: none;
  outline: none;
    image: url(:/dark_blue/img/radio_checked.png);
}

QRadioButton::indicator:checked:focus,
QRadioButton::indicato::menu-arrowr:checked:pressed
{
  border: none;
  outline: none;
    image: url(:/dark_blue/img/radio_checked_focus.png);
}

QRadioButton::indicator:indeterminate,
QRadioButton::indicator:indeterminate:hover,
QRadioButton::indicator:indeterminate:pressed
{
        image: url(:/dark_blue/img/radio_indeterminate.png);
}

QRadioButton::indicator:checked:disabled
{
  outline: none;
  image: url(:/dark_blue/img/radio_checked_disabled.png);
}

QRadioButton::indicator:unchecked:disabled
{
    image: url(:/dark_blue/img/radio_unchecked_disabled.png);
}


QMenuBar
{
    background-color: #302F2F;
    color: silver;
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #3A3939;
}

QMenuBar::item:pressed
{
    border: 1px solid #3A3939;
    background-color: #3d8ec9;
    color: black;
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #3A3939;
    color: silver;
    margin: 1px;
}

QMenu::icon
{
    margin: 1px;
}

QMenu::item
{
    padding: 2px 2px 2px 25px;
    margin-left: 5px;
    border: 1px solid transparent; /* reserve space for selection border */
}

QMenu::item:selected
{
    color: black;
}

QMenu::separator {
    height: 2px;
    background: lightblue;
    margin-left: 10px;
    margin-right: 5px;
}

QMenu::indicator {
    width: 16px;
    height: 16px;
}

/* non-exclusive indicator = check box style indicator
   (see QActionGroup::setExclusive) */
QMenu::indicator:non-exclusive:unchecked {
    image: url(:/dark_blue/img/checkbox_unchecked.png);
}

QMenu::indicator:non-exclusive:unchecked:selected {
    image: url(:/dark_blue/img/checkbox_unchecked_disabled.png);
}

QMenu::indicator:non-exclusive:checked {
    image: url(:/dark_blue/img/checkbox_checked.png);
}

QMenu::indicator:non-exclusive:checked:selected {
    image: url(:/dark_blue/img/checkbox_checked_disabled.png);
}

/* exclusive indicator = radio button style indicator (see QActionGroup::setExclusive) */
QMenu::indicator:exclusive:unchecked {
    image: url(:/dark_blue/img/radio_unchecked.png);
}

QMenu::indicator:exclusive:unchecked:selected {
    image: url(:/dark_blue/img/radio_unchecked_disabled.png);
}

QMenu::indicator:exclusive:checked {
    image: url(:/dark_blue/img/radio_checked.png);
}

QMenu::indicator:exclusive:checked:selected {
    image: url(:/dark_blue/img/radio_checked_disabled.png);
}

QMenu::right-arrow {
    margin: 5px;
    image: url(:/dark_blue/img/right_arrow.png)
}


QWidget:disabled
{
    color: #808080;
    background-color: #302F2F;
}

QAbstractItemView
{
    alternate-background-color: #3A3939;
    color: silver;
    border: 1px solid 3A3939;
    border-radius: 2px;
    padding: 1px;
}

QWidget:focus, QMenuBar:focus
{
    border: 1px solid #78879b;
}

QTabWidget:focus, QCheckBox:focus, QRadioButton:focus, QSlider:focus
{
    border: none;
}

QLineEdit
{
    background-color: #201F1F;
    padding: 2px;
    border-style: solid;
    border: 1px solid #3A3939;
    border-radius: 2px;
    color: silver;
}

QGroupBox {
    border:1px solid #3A3939;
    border-radius: 2px;
    margin-top: 20px;
    background-color: #302F2F;
    color: silver;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 10px;
}

QAbstractScrollArea
{
    border-radius: 2px;
    border: 1px solid #3A3939;
    background-color: transparent;
}

QScrollBar:horizontal
{
    height: 15px;
    margin: 3px 15px 3px 15px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
    background-color: #2A2929;
}

QScrollBar::handle:horizontal
{
    background-color: #605F5F;
    min-width: 5px;
    border-radius: 4px;
}

QScrollBar::add-line:horizontal
{
    margin: 0px 3px 0px 3px;
    border-image: url(:/dark_blue/img/right_arrow_disabled.png);
    width: 10px;
    height: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal
{
    margin: 0px 3px 0px 3px;
    border-image: url(:/dark_blue/img/left_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover,QScrollBar::add-line:horizontal:on
{
    border-image: url(:/dark_blue/img/right_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}


QScrollBar::sub-line:horizontal:hover, QScrollBar::sub-line:horizontal:on
{
    border-image: url(:/dark_blue/img/left_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{
    background: none;
}


QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
    background: none;
}

QScrollBar:vertical
{
    background-color: #2A2929;
    width: 15px;
    margin: 15px 3px 15px 3px;
    border: 1px transparent #2A2929;
    border-radius: 4px;
}

QScrollBar::handle:vertical
{
    background-color: #605F5F;
    min-height: 5px;
    border-radius: 4px;
}

QScrollBar::sub-line:vertical
{
    margin: 3px 0px 3px 0px;
    border-image: url(:/dark_blue/img/up_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical
{
    margin: 3px 0px 3px 0px;
    border-image: url(:/dark_blue/img/down_arrow_disabled.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:vertical:on
{

    border-image: url(:/dark_blue/img/up_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}


QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on
{
    border-image: url(:/dark_blue/img/down_arrow.png);
    height: 10px;
    width: 10px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
    background: none;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
    background: none;
}

QTextEdit
{
    background-color: #201F1F;
    color: silver;
    border: 1px solid #3A3939;
}

QPlainTextEdit
{
    background-color: #201F1F;;
    color: silver;
    border-radius: 2px;
    border: 1px solid #3A3939;
}

QHeaderView::section
{
    background-color: #3A3939;
    color: silver;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QSizeGrip {
    image: url(:/dark_blue/img/sizegrip.png);
    width: 12px;
    height: 12px;
}

QMainWindow
{
    background-color: #302F2F;

}

QMainWindow::separator
{
    background-color: #302F2F;
    color: white;
    padding-left: 4px;
    spacing: 2px;
    border: 1px dashed #3A3939;
}

QMainWindow::separator:hover
{

    background-color: #787876;
    color: white;
    padding-left: 4px;
    border: 1px solid #3A3939;
    spacing: 2px;
}


QMenu::separator
{
    height: 1px;
    background-color: #3A3939;
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}


QFrame
{
    border-radius: 2px;
    border: 1px solid #444;
}

QFrame[frameShape="0"]
{
    border-radius: 2px;
    border: 1px transparent #444;
}

QStackedWidget
{
    background-color: #302F2F;
    border: 1px transparent black;
}

QToolBar {
    border: 1px transparent #393838;
    background: 1px solid #302F2F;
    font-weight: bold;
}

QToolBar::handle:horizontal {
    image: url(:/dark_blue/img/Hmovetoolbar.png);
}
QToolBar::handle:vertical {
    image: url(:/dark_blue/img/Vmovetoolbar.png);
}
QToolBar::separator:horizontal {
    image: url(:/dark_blue/img/Hsepartoolbar.png);
}
QToolBar::separator:vertical {
    image: url(:/dark_blue/img/Vsepartoolbars.png);
}

QPushButton
{
    color: silver;
    background-color: #302F2F;
    border-width: 2px;
    border-color: #4A4949;
    border-style: solid;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 4px;
    /* outline: none; */
    /* min-width: 40px; */
}

QPushButton:disabled
{
    background-color: #302F2F;
    border-width: 2px;
    border-color: #3A3939;
    border-style: solid;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-left: 10px;
    padding-right: 10px;
    /*border-radius: 2px;*/
    color: #808080;
}

QPushButton:focus {
    background-color: #3d8ec9;
    color: white;
}

QComboBox
{
    selection-background-color: #3d8ec9;
    background-color: #201F1F;
    border-style: solid;
    border: 1px solid #3A3939;
    border-radius: 2px;
    padding: 2px;
    min-width: 75px;
}

QPushButton:checked{
    background-color: #4A4949;
    border-color: #6A6969;
}

QPushButton:hover {
    border: 2px solid #78879b;
    color: silver;
}

QComboBox:hover, QAbstractSpinBox:hover,QLineEdit:hover,QTextEdit:hover,QPlainTextEdit:hover,QAbstractView:hover,QTreeView:hover
{
    border: 1px solid #78879b;
    color: silver;
}

QComboBox:on
{
    background-color: #626873;
    padding-top: 3px;
    padding-left: 4px;
    selection-background-color: #4a4a4a;
}

QComboBox QAbstractItemView
{
    background-color: #201F1F;
    border-radius: 2px;
    border: 1px solid #444;
    selection-background-color: #3d8ec9;
    color: silver;
}

QComboBox::drop-down
{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 15px;

    border-left-width: 0px;
    border-left-color: darkgray;
    border-left-style: solid;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow
{
    image: url(:/dark_blue/img/down_arrow_disabled.png);
}

QComboBox::down-arrow:on, QComboBox::down-arrow:hover,
QComboBox::down-arrow:focus
{
    image: url(:/dark_blue/img/down_arrow.png);
}

QPushButton:pressed
{
    background-color: #484846;
}

QAbstractSpinBox {
    padding-top: 2px;
    padding-bottom: 2px;
    border: 1px solid #3A3939;
    background-color: #201F1F;
    color: silver;
    border-radius: 2px;
    min-width: 75px;
}

QAbstractSpinBox:up-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: top right;
}

QAbstractSpinBox:down-button
{
    background-color: transparent;
    subcontrol-origin: border;
    subcontrol-position: bottom right;
}

QAbstractSpinBox::up-arrow,QAbstractSpinBox::up-arrow:disabled,QAbstractSpinBox::up-arrow:off {
    image: url(:/dark_blue/img/up_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::up-arrow:hover
{
    image: url(:/dark_blue/img/up_arrow.png);
}


QAbstractSpinBox::down-arrow,QAbstractSpinBox::down-arrow:disabled,QAbstractSpinBox::down-arrow:off
{
    image: url(:/dark_blue/img/down_arrow_disabled.png);
    width: 10px;
    height: 10px;
}
QAbstractSpinBox::down-arrow:hover
{
    image: url(:/dark_blue/img/down_arrow.png);
}


QLabel
{
    border: 0px solid black;
}

QTabWidget{
    border: 1px transparent black;
}

QTabWidget::pane {
    border: 1px solid #444;
    border-radius: 3px;
    padding: 3px;
}

QTabBar
{
    qproperty-drawBase: 0;
    left: 5px; /* move to the right by 5px */
}

QTabBar:focus
{
    border: 0px transparent black;
}

QTabBar::close-button  {
    image: url(:/dark_blue/img/close.png);
    background: transparent;
}

QTabBar::close-button:hover
{
    image: url(:/dark_blue/img/close-hover.png);
    background: transparent;
}

QTabBar::close-button:pressed {
    image: url(:/dark_blue/img/close-pressed.png);
    background: transparent;
}

/* TOP TABS */
QTabBar::tab:top {
    color: #b1b1b1;
    border: 1px solid #4A4949;
    border-bottom: 1px transparent black;
    background-color: #302F2F;
    padding: 5px;
    border-top-left-radius: 2px;
    border-top-right-radius: 2px;
}

QTabBar::tab:top:!selected
{
    color: #b1b1b1;
    background-color: #201F1F;
    border: 1px transparent #4A4949;
    border-bottom: 1px transparent #4A4949;
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
}

QTabBar::tab:top:!selected:hover {
    background-color: #48576b;
}

/* BOTTOM TABS */
QTabBar::tab:bottom {
    color: #b1b1b1;
    border: 1px solid #4A4949;
    border-top: 1px transparent black;
    background-color: #302F2F;
    padding: 5px;
    border-bottom-left-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:bottom:!selected
{
    color: #b1b1b1;
    background-color: #201F1F;
    border: 1px transparent #4A4949;
    border-top: 1px transparent #4A4949;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}

QTabBar::tab:bottom:!selected:hover {
    background-color: #78879b;
}

/* LEFT TABS */
QTabBar::tab:left {
    color: #b1b1b1;
    border: 1px solid #4A4949;
    border-left: 1px transparent black;
    background-color: #302F2F;
    padding: 5px;
    border-top-right-radius: 2px;
    border-bottom-right-radius: 2px;
}

QTabBar::tab:left:!selected
{
    color: #b1b1b1;
    background-color: #201F1F;
    border: 1px transparent #4A4949;
    border-right: 1px transparent #4A4949;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
}

QTabBar::tab:left:!selected:hover {
    background-color: #48576b;
}


/* RIGHT TABS */
QTabBar::tab:right {
    color: #b1b1b1;
    border: 1px solid #4A4949;
    border-right: 1px transparent black;
    background-color: #302F2F;
    padding: 5px;
    border-top-left-radius: 2px;
    border-bottom-left-radius: 2px;
}

QTabBar::tab:right:!selected
{
    color: #b1b1b1;
    background-color: #201F1F;
    border: 1px transparent #4A4949;
    border-right: 1px transparent #4A4949;
    border-top-left-radius: 0px;
    border-bottom-left-radius: 0px;
}

QTabBar::tab:right:!selected:hover {
    background-color: #48576b;
}

QTabBar QToolButton::right-arrow:enabled {
     image: url(:/dark_blue/img/right_arrow.png);
 }

 QTabBar QToolButton::left-arrow:enabled {
     image: url(:/dark_blue/img/left_arrow.png);
 }

QTabBar QToolButton::right-arrow:disabled {
     image: url(:/dark_blue/img/right_arrow_disabled.png);
 }

 QTabBar QToolButton::left-arrow:disabled {
     image: url(:/dark_blue/img/left_arrow_disabled.png);
 }


QDockWidget {
    border: 1px solid #403F3F;
    titlebar-close-icon: url(:/dark_blue/img/close.png);
    titlebar-normal-icon: url(:/dark_blue/img/undock.png);
}

QDockWidget::close-button, QDockWidget::float-button {
    border: 1px solid transparent;
    border-radius: 2px;
    background: transparent;
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover {
    background: rgba(255, 255, 255, 10);
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed {
    padding: 1px -1px -1px 1px;
    background: rgba(255, 255, 255, 10);
}

QTreeView, QListView, QTextBrowser, AtLineEdit, AtLineEdit::hover {
    border: 1px solid #444;
    background-color: silver;
    border-radius: 3px;
    margin-left: 3px;
    color: black;
}

QTreeView:branch:selected, QTreeView:branch:hover {
    background: url(:/dark_blue/img/transparent.png);
}

QTreeView::branch:has-siblings:!adjoins-item {
    border-image: url(:/dark_blue/img/transparent.png);
}

QTreeView::branch:has-siblings:adjoins-item {
    border-image: url(:/dark_blue/img/transparent.png);
}

QTreeView::branch:!has-children:!has-siblings:adjoins-item {
    border-image: url(:/dark_blue/img/transparent.png);
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(:/dark_blue/img/branch_closed.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings  {
    image: url(:/dark_blue/img/branch_open.png);
}

QTreeView::branch:has-children:!has-siblings:closed:hover,
QTreeView::branch:closed:has-children:has-siblings:hover {
    image: url(:/dark_blue/img/branch_closed-on.png);
    }

QTreeView::branch:open:has-children:!has-siblings:hover,
QTreeView::branch:open:has-children:has-siblings:hover  {
    image: url(:/dark_blue/img/branch_open-on.png);
    }

QListView::item:!selected:hover, QListView::item:!selected:hover, QTreeView::item:!selected:hover  {
    background: rgba(0, 0, 0, 0);
    outline: 0;
    color: #FFFFFF
}

QListView::item:selected:hover, QListView::item:selected:hover, QTreeView::item:selected:hover  {
    background: #3d8ec9;
    color: #FFFFFF;
}

QSlider::groove:horizontal {
    border: 1px solid #3A3939;
    height: 8px;
    background: #201F1F;
    margin: 2px 0;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: -4px 0;
    border-radius: 2px;
}

QSlider::groove:vertical {
    border: 1px solid #3A3939;
    width: 8px;
    background: #201F1F;
    margin: 0 0px;
    border-radius: 2px;
}

QSlider::handle:vertical {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,
    stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: 0 -4px;
    border-radius: 2px;
}

QToolButton {
    /*  background-color: transparent; */
    border: 2px transparent #4A4949;
    border-radius: 4px;
    background-color: dimgray;
    margin: 2px;
    padding: 2px;
}

QToolButton[popupMode="1"] { /* only for MenuButtonPopup */
 padding-right: 20px; /* make way for the popup button */
 border: 2px transparent #4A4949;
 border-radius: 4px;
}

QToolButton[popupMode="2"] { /* only for InstantPopup */
 padding-right: 10px; /* make way for the popup button */
 border: 2px transparent #4A4949;
}


QToolButton:hover, QToolButton::menu-button:hover {
    border: 2px solid #78879b;
}

QToolButton:checked, QToolButton:pressed,
    QToolButton::menu-button:pressed {
    background-color: #4A4949;
    border: 2px solid #78879b;
}

/* the subcontrol below is used only in the InstantPopup or DelayedPopup mode */
QToolButton::menu-indicator {
    image: url(:/dark_blue/img/down_arrow.png);
    top: -7px; left: -2px; /* shift it a bit */
}

/* the subcontrols below are used only in the MenuButtonPopup mode */
QToolButton::menu-button {
    border: 1px transparent #4A4949;
    border-top-right-radius: 6px;
    border-bottom-right-radius: 6px;
    /* 16px width + 4px for border = 20px allocated above */
    width: 16px;
    outline: none;
}

QToolButton::menu-arrow {
    image: url(:/dark_blue/img/down_arrow.png);
}

QToolButton::menu-arrow:open {
    top: 1px; left: 1px; /* shift it a bit */
    border: 1px solid #3A3939;
}

QPushButton::menu-indicator  {
    subcontrol-origin: padding;
    subcontrol-position: bottom right;
    left: 4px;
}

QTableView
{
    border: 1px solid #444;
    gridline-color: #6c6c6c;
    background-color: #201F1F;
}


QTableView, QHeaderView
{
    border-radius: 0px;
}

QTableView::item:pressed, QListView::item:pressed, QTreeView::item:pressed  {
    background: #78879b;
    color: #FFFFFF;
}

QTableView::item:selected:active, QTreeView::item:selected:active, QListView::item:selected:active  {
    background: #3d8ec9;
    color: #FFFFFF;
}


QHeaderView
{
    border: 1px transparent;
    border-radius: 2px;
    margin: 0px;
    padding: 0px;
}

QHeaderView::section  {
    background-color: #3A3939;
    color: silver;
    padding: 4px;
    border: 1px solid #6c6c6c;
    border-radius: 0px;
    text-align: center;
}

QHeaderView::section::vertical::first, QHeaderView::section::vertical::only-one
{
    border-top: 1px solid #6c6c6c;
}

QHeaderView::section::vertical
{
    border-top: transparent;
}

QHeaderView::section::horizontal::first, QHeaderView::section::horizontal::only-one
{
    border-left: 1px solid #6c6c6c;
}

QHeaderView::section::horizontal
{
    border-left: transparent;
}


QHeaderView::section:checked
 {
    color: white;
    background-color: #5A5959;
 }

 /* style the sort indicator */
QHeaderView::down-arrow {
    image: url(:/dark_blue/img/down_arrow.png);
}

QHeaderView::up-arrow {
    image: url(:/dark_blue/img/up_arrow.png);
}


QTableCornerButton::section {
    background-color: #3A3939;
    border: 1px solid #3A3939;
    border-radius: 2px;
}

QToolBox  {
    padding: 3px;
    border: 1px transparent black;
}

QToolBox::tab {
    color: #b1b1b1;
    background-color: #302F2F;
    border: 1px solid #4A4949;
    border-bottom: 1px transparent #302F2F;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

 QToolBox::tab:selected { /* italicize selected tabs */
    font: italic;
    background-color: #302F2F;
    border-color: #3d8ec9;
 }

QStatusBar::item {
    border: 1px solid #3A3939;
    border-radius: 2px;
 }


QFrame[height="3"], QFrame[width="3"] {
    background-color: #AAA;
}


QSplitter::handle {
    border: 1px dashed #3A3939;
}

QSplitter::handle:hover {
    background-color: #787876;
    border: 1px solid #3A3939;
}

QSplitter::handle:horizontal {
    width: 1px;
}

QSplitter::handle:vertical {
    height: 1px;
}

QListWidget {
    background-color: silver;
    border-radius: 5px;
    margin-left: 5px;
}

QListWidget::item {
    color: black;
}

ColorButton::enabled {
    border-radius: 0px;
    border: 1px solid #444444;
}

ColorButton::disabled {
    border-radius: 0px;
    border: 1px solid #AAAAAA;
} """

# -----------------------------------------------------------------------------------------------
darkOrange = """ QToolTip
{
     border: 1px solid black;
     background-color: #ffa02f;
     padding: 1px;
     border-radius: 3px;
     opacity: 100;
}

QWidget
{
    color: #b1b1b1;
    background-color: #323232;
}

QTreeView, QListView
{
    background-color: silver;
    margin-left: 5px;
}

QWidget:item:hover
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);
    color: #000000;
}

QWidget:item:selected
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QMenuBar::item
{
    background: transparent;
}

QMenuBar::item:selected
{
    background: transparent;
    border: 1px solid #ffaa00;
}

QMenuBar::item:pressed
{
    background: #444;
    border: 1px solid #000;
    background-color: QLinearGradient(
        x1:0, y1:0,
        x2:0, y2:1,
        stop:1 #212121,
        stop:0.4 #343434/*,
        stop:0.2 #343434,
        stop:0.1 #ffaa00*/
    );
    margin-bottom:-1px;
    padding-bottom:1px;
}

QMenu
{
    border: 1px solid #000;
}

QMenu::item
{
    padding: 2px 20px 2px 20px;
}

QMenu::item:selected
{
    color: #000000;
}

QWidget:disabled
{
    color: #808080;
    background-color: #323232;
}

QAbstractItemView
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);
}

QWidget:focus
{
    /*border: 1px solid darkgray;*/
}

QLineEdit
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);
    padding: 1px;
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QPushButton
{
    color: #b1b1b1;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-width: 1px;
    border-color: #1e1e1e;
    border-style: solid;
    border-radius: 6;
    padding: 3px;
    font-size: 12px;
    padding-left: 5px;
    padding-right: 5px;
    min-width: 40px;
}

QPushButton:pressed
{
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
}

QComboBox
{
    selection-background-color: #ffaa00;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);
    border-style: solid;
    border: 1px solid #1e1e1e;
    border-radius: 5;
}

QComboBox:hover,QPushButton:hover
{
    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}


QComboBox:on
{
    padding-top: 3px;
    padding-left: 4px;
    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);
    selection-background-color: #ffaa00;
}

QComboBox QAbstractItemView
{
    border: 2px solid darkgray;
    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
}

QComboBox::drop-down
{
     subcontrol-origin: padding;
     subcontrol-position: top right;
     width: 15px;

     border-left-width: 0px;
     border-left-color: darkgray;
     border-left-style: solid; /* just a single line */
     border-top-right-radius: 3px; /* same radius as the QComboBox */
     border-bottom-right-radius: 3px;
 }

QComboBox::down-arrow
{
     image: url(:/dark_orange/img/down_arrow.png);
}

QGroupBox
{
    border: 1px solid darkgray;
    margin-top: 10px;
}

QGroupBox:focus
{
    border: 1px solid darkgray;
}

QTextEdit:focus
{
    border: 1px solid darkgray;
}

QScrollBar:horizontal {
     border: 1px solid #222222;
     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
     height: 7px;
     margin: 0px 16px 0 16px;
}

QScrollBar::handle:horizontal
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
      subcontrol-position: right;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal {
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);
      width: 14px;
     subcontrol-position: left;
     subcontrol-origin: margin;
}

QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{
      background: none;
}

QScrollBar:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);
      width: 7px;
      margin: 16px 0 16px 0;
      border: 1px solid #222222;
}

QScrollBar::handle:vertical
{
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);
      min-height: 20px;
      border-radius: 2px;
}

QScrollBar::add-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);
      height: 14px;
      subcontrol-position: bottom;
      subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical
{
      border: 1px solid #1b1b19;
      border-radius: 2px;
      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);
      height: 14px;
      subcontrol-position: top;
      subcontrol-origin: margin;
}

QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical
{
      border: 1px solid black;
      width: 1px;
      height: 1px;
      background: white;
}


QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical
{
      background: none;
}

QTextEdit
{
    background-color: #242424;
}

QPlainTextEdit
{
    background-color: #242424;
}

QHeaderView::section
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
}

QCheckBox:disabled
{
color: #414141;
}

QDockWidget::title
{
    text-align: center;
    spacing: 3px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button, QDockWidget::float-button
{
    text-align: center;
    spacing: 1px; /* spacing between items in the tool bar */
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);
}

QDockWidget::close-button:hover, QDockWidget::float-button:hover
{
    background: #242424;
}

QDockWidget::close-button:pressed, QDockWidget::float-button:pressed
{
    padding: 1px -1px -1px 1px;
}

QMainWindow::separator
{
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    border: 1px solid #4c4c4c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QMainWindow::separator:hover
{

    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);
    color: white;
    padding-left: 4px;
    border: 1px solid #6c6c6c;
    spacing: 3px; /* spacing between items in the tool bar */
}

QToolBar::handle
{
     spacing: 3px; /* spacing between items in the tool bar */
     background: url(:/dark_orange/img/handle.png);
}

QMenu::separator
{
    height: 2px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);
    color: white;
    padding-left: 4px;
    margin-left: 10px;
    margin-right: 5px;
}

QProgressBar
{
    border: 2px solid grey;
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk
{
    background-color: #d7801a;
    width: 2.15px;
    margin: 0.5px;
}

QTabBar::tab {
    color: #b1b1b1;
    border: 1px solid #444;
    border-bottom-style: none;
    background-color: #323232;
    padding-left: 10px;
    padding-right: 10px;
    padding-top: 3px;
    padding-bottom: 2px;
    margin-right: -1px;
}

QTabWidget::pane {
    border: 1px solid #444;
    top: 1px;
}

QTabBar::tab:last
{
    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */
    border-top-right-radius: 3px;
}

QTabBar::tab:first:!selected
{
 margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */


    border-top-left-radius: 3px;
}

QTabBar::tab:!selected
{
    color: #b1b1b1;
    border-bottom-style: solid;
    margin-top: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);
}

QTabBar::tab:selected
{
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    margin-bottom: 0px;
}

QTabBar::tab:!selected:hover
{
    /*border-top: 2px solid #ffaa00;
    padding-bottom: 3px;*/
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);
}

QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    border-radius: 6px;
}

QRadioButton::indicator:checked
{
    background-color: qradialgradient(
        cx: 0.5, cy: 0.5,
        fx: 0.5, fy: 0.5,
        radius: 1.0,
        stop: 0.25 #ffaa00,
        stop: 0.3 #323232
    );
}

QCheckBox::indicator{
    color: #b1b1b1;
    background-color: #323232;
    border: 1px solid #b1b1b1;
    width: 9px;
    height: 9px;
}

QRadioButton::indicator
{
    border-radius: 6px;
}

QRadioButton::indicator:hover, QCheckBox::indicator:hover
{
    border: 1px solid #ffaa00;
}

QCheckBox::indicator:checked
{
    image:url(:/dark_orange/img/checkbox.png);
}

QCheckBox::indicator:disabled, QRadioButton::indicator:disabled
{
    border: 1px solid #444;
}


QSlider::groove:horizontal {
    border: 1px solid #3A3939;
    height: 8px;
    background: #201F1F;
    margin: 2px 0;
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,
      stop: 0.0 silver, stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: -4px 0;
    border-radius: 2px;
}

QSlider::groove:vertical {
    border: 1px solid #3A3939;
    width: 8px;
    background: #201F1F;
    margin: 0 0px;
    border-radius: 2px;
}

QSlider::handle:vertical {
    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 silver,
      stop: 0.2 #a8a8a8, stop: 1 #727272);
    border: 1px solid #3A3939;
    width: 14px;
    height: 14px;
    margin: 0 -4px;
    border-radius: 2px;
}

QAbstractSpinBox {
    padding-top: 2px;
    padding-bottom: 2px;
    border: 1px solid darkgray;

    border-radius: 2px;
    min-width: 50px;
} """
