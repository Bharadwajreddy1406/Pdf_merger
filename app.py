#########################################3



import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QListWidget, QMessageBox
from PyPDF2 import PdfWriter, PdfReader
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 425)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Assets/icons/pngwing.com (13).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background:#f5f5fa")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 60, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background:transparent;\n"
                                  "color:#3b3b3b;\n"
                                  "")
        self.label.setObjectName("label")
        self.addbtn = QtWidgets.QPushButton(self.centralwidget)
        self.addbtn.setGeometry(QtCore.QRect(40, 60, 211, 211))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(28)
        self.addbtn.setFont(font)
        self.addbtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addbtn.setStyleSheet("background:white;\n"
                                  "border:3px solid #cfcfcf;\n"
                                  "border-radius:12px;")
        self.addbtn.setObjectName("addbtn")
        self.addbtn.clicked.connect(self.add_pdf)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:transparent;\n"
                                   "color:#3b3b3b;\n"
                                   "")
        self.file_list = QListWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.file_list)
        self.label_2.setObjectName("label_2")
        self.merge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.merge_btn.setGeometry(QtCore.QRect(370, 200, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.merge_btn.setFont(font)
        self.merge_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.merge_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.merge_btn.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.merge_btn.setStyleSheet("\n"
                                      "color:white;\n"
                                      "border-radius:8px;\n"
                                      "background:qlineargradient(spread:pad, x1:0, y1:0.25, x2:1, y2:0.989, stop:0 rgba(13, 138, 13, 255), stop:1 rgba(100, 255, 28, 255))")
        self.merge_btn.setObjectName("merge_btn")
        self.merge_btn.clicked.connect(self.merge_pdfs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.input_files = []

    def add_pdf(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("PDF files (*.pdf)")
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec_():
            files = file_dialog.selectedFiles()
            for file in files:
                self.input_files.append(file)

    def merge_pdfs(self):
        print("entered")
        if len(self.input_files) < 2:
            pass

            return

        output_path, _ = QFileDialog.getSaveFileName(self.centralwidget, 'Save Merged PDF', '', 'PDF files (*.pdf)')
        if output_path:
            pdf_writer = PdfWriter()

            for input_file in self.input_files:
                with open(input_file, 'rb') as pdf_file:
                    pdf_reader = PdfReader(pdf_file)
                    for page in pdf_reader.pages:
                        pdf_writer.add_page(page)

            with open(output_path, 'wb') as output_file:
                pdf_writer.write(output_file)

            QMessageBox.information(self.centralwidget, 'Success', 'PDF files merged successfully!')
            self.input_files.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF_merger"))
        self.label.setText(_translate("MainWindow", "Merge Your Pdf files Here"))
        self.addbtn.setText(_translate("MainWindow", "+"))
        self.label_2.setText(_translate("MainWindow", "Add Your files Here"))
        self.merge_btn.setText(_translate("MainWindow", "Click to Merge"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
