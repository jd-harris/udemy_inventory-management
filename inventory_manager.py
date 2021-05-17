from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

import main

import sys
import sqlite3
from os import path

import res_1  # Import resources file

import pyqt_themes


# LOAD UI into Python ISSUE***
# CONVERTING UI file to Python works better
# from PySide2.QtUiTools import QUiLoader

# loader = QUiLoader()

# FORM_CLASS, _ = QUiLoader.load(path.join(path.dirname('__file__'), "main.ui"))
# window = loader.load("main.ui", None)
x = 0
idx = 2


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for Pyinstaller """
    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    return path.join(base_path, relative_path)


class Main(QtWidgets.QMainWindow, main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.handle_buttons()

    def handle_buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.SEARCH)
        self.check_btn.clicked.connect(self.LEVEL)
        self.update_btn.clicked.connect(self.UPDATE)
        self.delete_btn.clicked.connect(self.DELETE)
        self.add_btn.clicked.connect(self.ADD)
        self.first_btn.clicked.connect(self.FIRST)
        self.previous_btn.clicked.connect(self.PREVIOUS)
        self.next_btn.clicked.connect(self.NEXT)
        self.last_btn.clicked.connect(self.LAST)
        self.theme1_btn.clicked.connect(self.CHANGE_THEME1)
        self.theme2_btn.clicked.connect(self.CHANGE_THEME2)

    def GET_DATA(self):
        # Connect to Sqlite3 database and fill GUI table with data

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = ''' SELECT * from parts_table '''

        result = cursor.execute(command)

        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))  # nopep8

        # Display references number and type number in Statistics tab
        cursor2 = db.cursor()
        cursor3 = db.cursor()

        parts_nbr = ''' SELECT COUNT (DISTINCT PartName) from parts_table '''
        ref_nbr = ''' SELECT COUNT (DISTINCT Reference) from parts_table '''

        result_ref_nbr = cursor2.execute(ref_nbr)
        result_parts_nbr = cursor3.execute(parts_nbr)

        self.lbl_ref_nbr.setText(str(result_ref_nbr.fetchone()[0]))
        self.lbl_parts_nbr.setText(str(result_parts_nbr.fetchone()[0]))

        # Display 4 results: Min, Max Nbr of holes in addition to their respective reference names
        cursor4 = db.cursor()
        cursor5 = db.cursor()

        min_hole = ''' SELECT MIN (NumberOfHoles), Reference from parts_table '''
        max_hole = ''' SELECT MAX (NumberOfHoles), Reference from parts_table '''

        result_min_hole = cursor4.execute(min_hole)
        result_max_hole = cursor5.execute(max_hole)

        r1 = result_min_hole.fetchone()
        r2 = result_max_hole.fetchone()

        self.lbl_min_holes.setText(str(r1[0]))
        self.lbl_max_holes.setText(str(r2[0]))
        self.lbl_min_holes2.setText(str(r1[1]))
        self.lbl_max_holes2.setText(str(r2[1]))

        # Conditional change of Widget Style using Python Code
        if int(self.lbl_ref_nbr.text()) < 15:
            self.lbl_ref_nbr.setStyleSheet(""" QWidget{background-color: rgb(255, 0, 0); color: rgb(255, 255, 255);}""")  # nopep8

        self.FIRST()
        self.NAVIGATE()

    def SEARCH(self):
        # Connect to Sqlite3 database and fill GUI table with data
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        nbr = int(self.count_filter_txt.text())

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = ''' SELECT * from parts_table WHERE count<=?'''

        result = cursor.execute(command, [nbr])

        self.table.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))  # nopep8

    def LEVEL(self):
        # Connect to Sqlite3 database and fill GUI table with data
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = ''' SELECT Reference, PartName, Count from parts_table order by Count asc LIMIT 3 '''

        result = cursor.execute(command)

        self.table2.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.table2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))  # nopep8

    def NAVIGATE(self):
        global idx
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = '''SELECT * from parts_table WHERE ID=?'''

        result = cursor.execute(command, [idx])
        val = result.fetchone()

        self.id.setText(str(val[0]))
        self.reference.setText(str(val[1]))
        self.part_name.setText(str(val[2]))
        self.min_area.setText(str(val[3]))
        self.max_area.setText(str(val[4]))
        self.number_of_holes.setText(str(val[5]))
        self.min_diameter.setText(str(val[6]))
        self.max_diameter.setText(str(val[7]))
        self.count.setValue(val[8])

    def NEXT(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = '''SELECT ID from parts_table '''

        result = cursor.execute(command)
        val = result.fetchall()
        tot = len(val)
        global x
        global idx
        x = x+1
        if x < tot:
            idx = val[x][0]
            self.NAVIGATE()
        else:
            x = tot-1

    def PREVIOUS(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = '''SELECT ID from parts_table '''

        result = cursor.execute(command)
        val = result.fetchall()
        global x
        global idx
        x = x-1
        if x > -1:
            idx = val[x][0]
            self.NAVIGATE()
        else:
            x = 0

    def LAST(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = '''SELECT ID from parts_table '''

        result = cursor.execute(command)
        val = result.fetchall()
        tot = len(val)
        global x
        global idx
        x = tot-1
        if x < tot:
            idx = val[x][0]
            self.NAVIGATE()
        else:
            x = tot-1

    def FIRST(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        command = '''SELECT ID from parts_table '''

        result = cursor.execute(command)
        val = result.fetchall()
        global x
        global idx
        x = 0
        if x > -1:
            idx = val[x][0]
            self.NAVIGATE()
        else:
            x = 0

    def UPDATE(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        id_ = int(self.id.text())
        reference_ = self.reference.text()
        part_name_ = self.part_name.text()
        min_area_ = self.min_area.text()
        max_area_ = self.max_area.text()
        number_of_holes_ = self.number_of_holes.text()
        min_diameter_ = self.min_diameter.text()
        max_diameter_ = self.max_diameter.text()
        count_ = str(self.count.value())

        row = (reference_, part_name_, min_area_, max_area_,
               number_of_holes_, min_diameter_, max_diameter_, count_, id_)

        command = ''' UPDATE parts_table SET Reference=?, PartName=?, MinArea=?, MaxArea=?, NumberOfHoles=?, MinDiameter=?, MaxDiameter=?, Count=? WHERE ID=?'''  # nopep8

        cursor.execute(command, row)

        db.commit()

    def DELETE(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        d = self.id.text()

        command = ''' DELETE FROM parts_table WHERE ID=? '''

        cursor.execute(command, d)

        db.commit()

    def ADD(self):
        # BASE_DIR = path.dirname(path.abspath(__file__))
        # db_path = path.join(BASE_DIR, "parts.db")

        db = sqlite3.connect(resource_path("parts.db"))
        cursor = db.cursor()

        reference_ = self.reference.text()
        part_name_ = self.part_name.text()
        min_area_ = self.min_area.text()
        max_area_ = self.max_area.text()
        number_of_holes_ = self.number_of_holes.text()
        min_diameter_ = self.min_diameter.text()
        max_diameter_ = self.max_diameter.text()
        count_ = str(self.count.value())

        row = (reference_, part_name_, min_area_, max_area_, number_of_holes_, min_diameter_, max_diameter_, count_)  # nopep8

        command = ''' INSERT INTO parts_table (Reference, PartName, MinArea, MaxArea, NumberOfHoles, MinDiameter, MaxDiameter, Count) VALUES (?, ?, ?, ?, ?, ?, ?, ?) '''  # nopep8

        cursor.execute(command, row)

        db.commit()

    def CHANGE_THEME1(self):
        self.setStyleSheet(pyqt_themes.classic)
        # self.update()

    def CHANGE_THEME2(self):
        self.setStyleSheet(pyqt_themes.darkBlue)
        # self.update()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
