import os
import sys
import re
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, uic
import warnings

# Ignore warnings
warnings.simplefilter("ignore", DeprecationWarning)

# Try to import bulkqtUi, handle missing module case
Ui_MainWindow = None
try:
    from bulkqtUi import Ui_MainWindow
except ImportError:
    Ui_MainWindow = None

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()

        self.ui = None
        if os.path.exists("bulkgui.ui"):
            uic.loadUi("bulkgui.ui", self)
        elif Ui_MainWindow is not None:
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
        else:
            QMessageBox.critical(self, "Error", "No UI file or Python UI class found! Application cannot run.")
            sys.exit(1)
        
        self.show()
        
        self.directory = "."
        self.listModel = QStandardItemModel()
        self.selectModel = QStandardItemModel()
        
        if self.ui:
            self.ui.selectView.setModel(self.selectModel)
        else:
            self.selectView.setModel(self.selectModel)
        
        self.selected = []
        
        # Connect Buttons and Actions
        self.get_ui_element("actionOpen").triggered.connect(self.load_directory)
        self.get_ui_element("filterButton").clicked.connect(self.filter_list)
        self.get_ui_element("selectButton").clicked.connect(self.choose_selection)
        self.get_ui_element("removeButton").clicked.connect(self.remove_selection)
        self.get_ui_element("applyButton").clicked.connect(self.rename_files)
        self.get_ui_element("extensionButton").clicked.connect(self.change_extension)
    
    def get_ui_element(self, name):
        return getattr(self.ui, name) if self.ui else getattr(self, name)
    
    def load_directory(self):
        try:
            self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
            self.listModel.clear()
            for file in os.listdir(self.directory):
                if os.path.isfile(os.path.join(self.directory, file)):
                    self.listModel.appendRow(QStandardItem(file))
            self.get_ui_element("listview").setModel(self.listModel)
        except Exception as e:
            print(e)

    def rename_files(self):
        counter = 1
        try:
            for filename in self.selected:
                filetype = filename.split('.')[-1]
                new_name = filename
                
                if self.get_ui_element("addfirstRadio").isChecked():
                    new_name = self.get_ui_element("renameEntry").text() + filename
                elif self.get_ui_element("removefirstRadio").isChecked() and filename.startswith(self.get_ui_element("renameEntry").text()):
                    new_name = filename[len(self.get_ui_element("renameEntry").text()):]
                elif self.get_ui_element("addlastRadio").isChecked():
                    new_name = filename[:-(len(filetype) + 1)] + self.get_ui_element("renameEntry").text() + "." + filetype
                elif self.get_ui_element("removelastRadio").isChecked() and filename.endswith(self.get_ui_element("renameEntry").text() + "." + filetype):
                    new_name = filename[:-len(self.get_ui_element("renameEntry").text() + '.' + filetype)] + "." + filetype
                elif self.get_ui_element("newnameRadio").isChecked():
                    new_name = self.get_ui_element("renameEntry").text() + str(counter) + "." + filetype
                    counter += 1
                
                os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, new_name))
                
            self.refresh_list()
        except Exception as e:
            print(e)
    
    def refresh_list(self):
        self.selected.clear()
        self.selectModel.clear()
        self.listModel.clear()
        for file in os.listdir(self.directory):
            if os.path.isfile(os.path.join(self.directory, file)):
                self.listModel.appendRow(QStandardItem(file))
        self.get_ui_element("listview").setModel(self.listModel)
    
    def choose_selection(self):
        for index in self.get_ui_element("listview").selectedIndexes():
            if index.data() not in self.selected:
                self.selected.append(index.data())
                self.selectModel.appendRow(QStandardItem(index.data()))
    
    def remove_selection(self):
        try:
            for index in reversed(sorted(self.get_ui_element("selectView").selectedIndexes())):
                self.selected.remove(index.data())
                self.selectModel.removeRow(index.row())
        except Exception as e:
            print(e)
    
    def filter_list(self):
        self.selectModel.clear()
        self.selected.clear()
        for index in range(self.listModel.rowCount()):
            item = self.listModel.item(index)
            if re.match(self.get_ui_element("searchEntry").text(), item.text()):
                self.selectModel.appendRow(QStandardItem(item.text()))
                self.selected.append(item.text())
    
    def change_extension(self):
        try:
            new_extension = self.get_ui_element("extensionEntry").text()
            if not new_extension.startswith('.'): new_extension = '.' + new_extension
            for index in range(self.selectModel.rowCount()):
                item = self.selectModel.item(index)
                filename = item.text()
                base_name, _ = os.path.splitext(filename)
                new_filename = base_name + new_extension
                os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, new_filename))
                item.setText(new_filename)
            self.refresh_list()
        except Exception as e:
            print(e)

app = QApplication(sys.argv)
window = MyGUI()
sys.exit(app.exec_())
