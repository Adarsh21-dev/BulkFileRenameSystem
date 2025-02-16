# Import all modules
from PyQt5 import QtCore, QtGui, QtWidgets

# create class for main_ui
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 791)
        MainWindow.setMinimumSize(QtCore.QSize(1020, 791))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 791))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        
        # define mainWindow Widgets ui
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # AppName
        self.appNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.appNameLabel.setGeometry(QtCore.QRect(0, 0, 1021, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        self.appNameLabel.setFont(font)
        self.appNameLabel.setStyleSheet("background-color: rgb(30, 144, 255);")
        self.appNameLabel.setObjectName("appNameLabel")
        
        # CreditsLabel
        self.creditsLabel = QtWidgets.QLabel(self.centralwidget)
        self.creditsLabel.setGeometry(QtCore.QRect(0, 60, 1021, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setAutoFillBackground(False)
        self.creditsLabel.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.creditsLabel.setObjectName("creditsLabel")
        
        # IconLabel
        self.iconLabel = QtWidgets.QLabel(self.centralwidget)
        self.iconLabel.setGeometry(QtCore.QRect(20, 100, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.iconLabel.setFont(font)
        self.iconLabel.setStyleSheet("")
        self.iconLabel.setObjectName("iconLabel")
        
        # SearchEntry
        self.searchEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.searchEntry.setGeometry(QtCore.QRect(170, 110, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.searchEntry.setFont(font)
        self.searchEntry.setText("")
        self.searchEntry.setObjectName("searchEntry")
        
        # FilterButton
        self.filterButton = QtWidgets.QPushButton(self.centralwidget)
        self.filterButton.setGeometry(QtCore.QRect(450, 110, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.filterButton.setFont(font)
        self.filterButton.setStyleSheet("background-color: rgb(30, 144, 255);\n"
"color: rgb(255, 255, 255);")
        self.filterButton.setObjectName("filterButton")
        
        # ExtensionEntry
        self.extensionEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.extensionEntry.setGeometry(QtCore.QRect(590, 110, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.extensionEntry.setFont(font)
        self.extensionEntry.setText("")
        self.extensionEntry.setObjectName("extensionEntry")
        self.extensionButton = QtWidgets.QPushButton(self.centralwidget)
        self.extensionButton.setGeometry(QtCore.QRect(780, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.extensionButton.setFont(font)
        self.extensionButton.setStyleSheet("background-color: rgb(30, 144, 255);\n"
"color: rgb(255, 255, 255);")
        self.extensionButton.setObjectName("extensionButton")
        
        # Horizontal Line
        self.hrLine = QtWidgets.QFrame(self.centralwidget)
        self.hrLine.setGeometry(QtCore.QRect(10, 150, 1001, 16))
        self.hrLine.setStyleSheet("color: rgb(51, 51, 51);\n"
"")
        self.hrLine.setFrameShadow(QtWidgets.QFrame.Plain)
        self.hrLine.setLineWidth(2)
        self.hrLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.hrLine.setObjectName("hrLine")
        
        # Listview or Listbox-1
        self.listview = QtWidgets.QListView(self.centralwidget)
        self.listview.setGeometry(QtCore.QRect(50, 170, 451, 361))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        self.listview.setFont(font)
        self.listview.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listview.setObjectName("listview")
        
        # Selectview or Listbox-2
        self.selectView = QtWidgets.QListView(self.centralwidget)
        self.selectView.setGeometry(QtCore.QRect(530, 170, 441, 361))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(12)
        self.selectView.setFont(font)
        self.selectView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selectView.setObjectName("selectView")
        
        # SelectButton
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(50, 540, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.selectButton.setFont(font)
        self.selectButton.setStyleSheet("background-color: rgb(30, 144, 255);\n"
"color: rgb(255, 255, 255);")
        self.selectButton.setObjectName("selectButton")
        
        # Remove Button
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(530, 540, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.removeButton.setFont(font)
        self.removeButton.setStyleSheet("background-color: rgb(30, 144, 255);\n"
"color: rgb(255, 255, 255);")
        self.removeButton.setObjectName("removeButton")
        
        # Choose Info Label
        self.chooseLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseLabel.setGeometry(QtCore.QRect(0, 590, 1021, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(11)
        self.chooseLabel.setFont(font)
        self.chooseLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(51, 51, 51);")
        self.chooseLabel.setObjectName("chooseLabel")
        
        # Add First Radio
        self.addfirstRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.addfirstRadio.setGeometry(QtCore.QRect(70, 650, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addfirstRadio.setFont(font)
        self.addfirstRadio.setObjectName("addfirstRadio")
        
        # Remove First Radio
        self.removefirstRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.removefirstRadio.setGeometry(QtCore.QRect(230, 650, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.removefirstRadio.setFont(font)
        self.removefirstRadio.setObjectName("removefirstRadio")
        
        # Add Last Radio
        self.addlastRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.addlastRadio.setGeometry(QtCore.QRect(440, 650, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.addlastRadio.setFont(font)
        self.addlastRadio.setObjectName("addlastRadio")
        
        # Remove Last Radio
        self.removelastRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.removelastRadio.setGeometry(QtCore.QRect(600, 650, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.removelastRadio.setFont(font)
        self.removelastRadio.setObjectName("removelastRadio")
        
        # Add Newname Radio
        self.newnameRadio = QtWidgets.QRadioButton(self.centralwidget)
        self.newnameRadio.setGeometry(QtCore.QRect(780, 650, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.newnameRadio.setFont(font)
        self.newnameRadio.setObjectName("newnameRadio")
        
        # Apply button or Rename Button
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(690, 690, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.applyButton.setFont(font)
        self.applyButton.setStyleSheet("background-color: rgb(30, 144, 255);\n"
"color: rgb(255, 255, 255);")
        self.applyButton.setObjectName("applyButton")
        
        # Rename Entry
        self.renameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.renameEntry.setGeometry(QtCore.QRect(230, 690, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Liberation Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.renameEntry.setFont(font)
        self.renameEntry.setText("")
        self.renameEntry.setObjectName("renameEntry")
        
        # Reaname Msg Label
        self.renameMsgLabel = QtWidgets.QLabel(self.centralwidget)
        self.renameMsgLabel.setGeometry(QtCore.QRect(60, 690, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.renameMsgLabel.setFont(font)
        self.renameMsgLabel.setObjectName("renameMsgLabel")
        
        # Menubar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 26))
        self.menubar.setObjectName("menubar")
        
        # MenuFile
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # ActionOpen Or Open Directory
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Css Work For PyQt5 Ui Design Function
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bulk Rename System"))
        self.appNameLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Bulk File Rename System</span></p></body></html>"))
        self.creditsLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Made By: Adarsh Kumar</span></p></body></html>"))
        self.iconLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#1e90ff;\">🪶🇧🇫🇫🇷🇸</span></p></body></html>"))
        self.filterButton.setText(_translate("MainWindow", "Filter"))
        self.extensionButton.setText(_translate("MainWindow", "Change Extension"))
        self.selectButton.setText(_translate("MainWindow", "Side Selection"))
        self.removeButton.setText(_translate("MainWindow", "Side Remove"))
        self.chooseLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Choose Any One Operation &amp; Apply Changes</p></body></html>"))
        self.addfirstRadio.setText(_translate("MainWindow", "Add First"))
        self.removefirstRadio.setText(_translate("MainWindow", "Remove First"))
        self.addlastRadio.setText(_translate("MainWindow", "Add Last"))
        self.removelastRadio.setText(_translate("MainWindow", "Remove Last"))
        self.newnameRadio.setText(_translate("MainWindow", "Add NewName"))
        self.applyButton.setText(_translate("MainWindow", "Apply Changes/Rename"))
        self.renameMsgLabel.setText(_translate("MainWindow", "Rename Here:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open Directory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
