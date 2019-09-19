import sys
from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMdiSubWindow, QLabel, QLineEdit, QPushButton, QLCDNumber, QWidget, QAction, QMessageBox

from lab03.exe01 import *

class Exercise01(QMdiSubWindow):

	x = 621
	y = 265

	def __init__(self, parent=None):
		QMdiSubWindow.__init__(self, parent)

		self.setWindowTitle("Ejercicio 1")

		self.lblOption = QLabel(self)
		self.lblOption.setGeometry(250, 50, 131, 21)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lblOption.setFont(font)
		self.lblOption.setText("Elegir una opción: ")

		self.btnPromedio = QPushButton(self)
		self.btnPromedio.setGeometry(90, 90, 91, 31)
		self.btnPromedio.setStyleSheet("font-weight: bold")
		self.btnPromedio.setText("Promedio")
		self.btnPromedio.clicked.connect(self.average)

		self.btnRoberts = QPushButton(self)
		self.btnRoberts.setGeometry(210, 90, 81, 31)
		self.btnRoberts.setStyleSheet("font-weight: bold")
		self.btnRoberts.setText("Roberts")
		self.btnRoberts.clicked.connect(self.roberts)

		self.btnPrewit = QPushButton(self)
		self.btnPrewit.setGeometry(330, 90, 81, 31)
		self.btnPrewit.setStyleSheet("font-weight: bold")
		self.btnPrewit.setText("Prewit")
		self.btnPrewit.clicked.connect(self.prewit)

		self.btnSobel = QPushButton(self)
		self.btnSobel.setGeometry(450, 90, 81, 31)
		self.btnSobel.setStyleSheet("font-weight: bold")
		self.btnSobel.setText("Sobel")
		self.btnSobel.clicked.connect(self.sobel)

		self.btnDelete = QPushButton(self)
		self.btnDelete.setGeometry(270, 150, 91, 41)
		self.btnDelete.setStyleSheet("font-weight: bold;\n""background-color: red")
		self.btnDelete.setText("BORRAR")
		self.btnDelete.clicked.connect(self.delete)

	def showMessage(self, text):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setText(text)
		msgBox.setWindowTitle("Info")

		msgBox.exec()

	def average(self):
		selectFilter(1)

	def roberts(self):
		selectFilter(2)

	def prewit(self):
		selectFilter(3)

	def sobel(self):
		selectFilter(4)

	def delete(self):
		deleteImages()
		self.showMessage("Las imágenes han sido borradas")