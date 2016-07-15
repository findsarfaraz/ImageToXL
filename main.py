from PyQt4 import QtGui,QtCore

from imgtoxl import Ui_MainWindow
import imgtoxl
import os
import openpyxl
from PIL import Image
import PIL
FilePath=""
FileName=""
FileDir=""

class create_xl(QtGui.QMainWindow,imgtoxl.Ui_MainWindow):
    def __init__(self):
        # super(create_xl,self).__init__()
        super(create_xl, self).__init__()
        self.setupUi(self)
        self.btn_Open_File.clicked.connect(self.OpenButton)
        self.btn_Save_File.clicked.connect(self.SaveButton)

    def OpenButton(self):
        global FilePath
        FilePath= QtGui.QFileDialog.getOpenFileName(self, ("Open File"),
                                               "C:\\",
                                               ("Images (*.png *.bmp *.jpg)"))

        FilePath = FilePath.replace("/","\\")
        self.lineEdit.setText(FilePath)

    def SaveButton(self):
        global FilePath
        global FileName
        global FileDir
        self.progressBar.setVisible(1)
        FileName = QtCore.QFileInfo(FilePath).fileName()

        FileName = FileName.replace(" ", "")
        FileDir=os.path.abspath(FilePath)
        FileDir=FileDir.replace(FileName,'')

        os.chdir(FileDir)
        img = Image.open(os.path.join(FileDir, str(FileName)))
        # pix = img.load()
        img_width = img.size[0]
        img_height = img.size[1]

        if img_width > 640:
            new_img_width = 640
            new_img_height = img_height * (1 - float((img_width - new_img_width)) / float(img_width))

        if img_height > 480:
            new_img_height = 480
            new_img_width = img_width * (1 - float((img_height - new_img_height)) / float(img_height))

        resized_img = img.resize((int(new_img_width), int(new_img_height)), PIL.Image.ANTIALIAS)
        pix = resized_img.load()

        dimension = new_img_width * new_img_height
        wb = openpyxl.Workbook()
        ws = wb.active
        counter = new_img_height


        for x in range(1, int(new_img_width)):
            for y in range(1, int(new_img_height)):
                clr = pix[x, y]
                val = ''.join(map(str, clr))
                ws.cell(row=y, column=x).value = int(val)
                counter = counter + 1
                pvalue = round(float(counter) / float(dimension) * 99, 0)
                self.progressBar.setValue(pvalue)
            counter = counter + 1


        ReverseFileName = str(FileName)[::-1]
        XLFileName = ReverseFileName[ReverseFileName.find(".") + 1::] + ".xlsx"

        wb.save(os.path.join(FileDir, str(XLFileName)))
        pvalue = 100
        self.progressBar.setValue(pvalue)

        XLFilePath = FileDir + str(XLFileName)
        msgString= "Your image has been encoded to MS Excel File %s at location:" %XLFilePath
        infoString= "Open file->set conditional formatting -> zoomout to see picture in MS Excel"

        ret =QtGui.QMessageBox.information(self,msgString,infoString,QtGui.QMessageBox.Ok)

        if ret == 1024:
            self.lineEdit.setText("")
            self.progressBar.setValue(0)
            if self.progressBar.isVisible():
                self.progressBar.setVisible(0)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = create_xl()
    form.show()
    app.exec_()
