# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imgtoxl.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(590, 96)
        MainWindow.setMaximumSize(QtCore.QSize(590, 96))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(11)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 411, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(2, 70, 583, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.btn_Open_File = QtGui.QPushButton(self.centralwidget)
        self.btn_Open_File.setGeometry(QtCore.QRect(500, 10, 75, 23))
        self.btn_Open_File.setObjectName(_fromUtf8("btn_Open_File"))
        self.btn_Save_File = QtGui.QPushButton(self.centralwidget)
        self.btn_Save_File.setGeometry(QtCore.QRect(500, 40, 75, 23))
        self.btn_Save_File.setObjectName(_fromUtf8("btn_Save_File"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.progressBar.setVisible(0)

        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "ImgToXL", None))
        self.label.setText(_translate("MainWindow", "Image File", None))
        self.btn_Open_File.setText(_translate("MainWindow", "Select File", None))
        self.btn_Save_File.setText(_translate("MainWindow", "Save File", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

