
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from lab03.exe01 import *

class Index(QTabWidget):
	''' Interfaz que conecta la GUI principal con los ejercicios del laboratorio 3 '''

	x = 960
	y = 635

	def __init__(self, parent=None):
		QTabWidget.__init__(self, parent)
		self.setWindowTitle("Laboratorio 1")

		self.tab1 = QtWidgets.QWidget()
		self.tab2 = QtWidgets.QWidget()

		self.addTab(self.tab1, "Ejercicio 1")
		self.addTab(self.tab2, "Tarea 1")
		
		#QTabBar::tab:selected {background: #F0F0F0;}
		self.setStyleSheet("""QTabWidget>QWidget>QWidget{background: #F0F0F0;}""")

		self.exercise01()
		self.homework01()



	def exercise01(self):

		self.lblOption = QtWidgets.QLabel(self.tab1)
		self.lblOption.setGeometry(430, 50, 131, 21)
		font = QtGui.QFont()
		font.setPointSize(12)
		self.lblOption.setFont(font)
		self.lblOption.setText("Elegir una opción: ")

		self.btnAverage = QtWidgets.QPushButton(self.tab1)
		self.btnAverage.setGeometry(260, 90, 91, 31)
		self.btnAverage.setStyleSheet("font-weight: bold")
		self.btnAverage.setText("Promedio")
		self.btnAverage.clicked.connect(self.average)

		self.btnRoberts = QtWidgets.QPushButton(self.tab1)
		self.btnRoberts.setGeometry(380, 90, 81, 31)
		self.btnRoberts.setStyleSheet("font-weight: bold")
		self.btnRoberts.setText("Roberts")
		self.btnRoberts.clicked.connect(self.roberts)

		self.btnPrewitt = QtWidgets.QPushButton(self.tab1)
		self.btnPrewitt.setGeometry(500, 90, 81, 31)
		self.btnPrewitt.setStyleSheet("font-weight: bold")
		self.btnPrewitt.setText("Prewit")
		self.btnPrewitt.clicked.connect(self.prewit)

		self.btnSobel = QtWidgets.QPushButton(self.tab1)
		self.btnSobel.setGeometry(620, 90, 81, 31)
		self.btnSobel.setStyleSheet("font-weight: bold")
		self.btnSobel.setText("Sobel")
		self.btnSobel.clicked.connect(self.sobel)

		self.btnDelete = QtWidgets.QPushButton(self.tab1)
		self.btnDelete.setGeometry(440, 150, 91, 41)
		self.btnDelete.setStyleSheet("font-weight: bold;\n""background-color: red")
		self.btnDelete.setText("BORRAR")
		self.btnDelete.clicked.connect(self.delete)

	def showMessage(self, text):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
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
		self.lblImg.setPixmap(QtGui.QPixmap("img/machu_picchu.jpg"))
		self.showMessage("Las imágenes han sido borradas")



	def homework01(self):
		self.btnAvera = QtWidgets.QPushButton(self.tab2)
		self.btnAvera.setGeometry(20, 30, 91, 31)
		self.btnAvera.setStyleSheet("font-weight: bold")
		self.btnAvera.setText("Promedio")
		self.btnAvera.clicked.connect(self.avera)

		self.btnRober = QtWidgets.QPushButton(self.tab2)
		self.btnRober.setGeometry(20, 80, 91, 31)
		self.btnRober.setStyleSheet("font-weight: bold")
		self.btnRober.setText("Roberts")
		self.btnRober.clicked.connect(self.rober)

		self.btnPrew = QtWidgets.QPushButton(self.tab2)
		self.btnPrew.setGeometry(20, 130, 91, 31)
		self.btnPrew.setStyleSheet("font-weight: bold")
		self.btnPrew.setText("Prewit")
		self.btnPrew.clicked.connect(self.prew)

		self.btnSob = QtWidgets.QPushButton(self.tab2)
		self.btnSob.setGeometry(20, 180, 91, 31)
		self.btnSob.setStyleSheet("font-weight: bold")
		self.btnSob.setText("Sobel")
		self.btnSob.clicked.connect(self.sob)

		self.btnDelete = QtWidgets.QPushButton(self.tab2)
		self.btnDelete.setGeometry(20, 230, 91, 41)
		self.btnDelete.setStyleSheet("font-weight: bold;\n""background-color: red")
		self.btnDelete.setText("BORRAR")
		self.btnDelete.clicked.connect(self.delete)

		self.lblImg = QtWidgets.QLabel(self.tab2)
		self.lblImg.setGeometry(130, 30, 800, 533)
		self.lblImg.setText("")
		self.lblImg.setPixmap(QtGui.QPixmap("img/machu_picchu.jpg"))

	def avera(self):
		selectFilter(1, False)
		self.lblImg.setPixmap(QtGui.QPixmap("img/promedio.tif"))

	def rober(self):
		selectFilter(2, False)
		self.lblImg.setPixmap(QtGui.QPixmap("img/roberts.tif"))

	def prew(self):
		selectFilter(3, False)
		self.lblImg.setPixmap(QtGui.QPixmap("img/prewitt.tif"))

	def sob(self):
		selectFilter(4, False)
		self.lblImg.setPixmap(QtGui.QPixmap("img/sobel.tif"))