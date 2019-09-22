
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from lab01.exe01 import *
from lab01.exe02 import *

class Index(QTabWidget):
	''' Interfaz que conecta la GUI principal con los ejercicios del laboratorio 1 '''

	x = 500
	y = 400

	def __init__(self, parent=None):
		QTabWidget.__init__(self, parent)
		self.setWindowTitle("Laboratorio 1")

		self.tab1 = QtWidgets.QWidget()
		self.tab2 = QtWidgets.QWidget()

		self.addTab(self.tab1, "Ejercicio 1")
		self.addTab(self.tab2, "Ejercicio 2")
		
		#QTabBar::tab:selected {background: #F0F0F0;}
		self.setStyleSheet("""QTabWidget>QWidget>QWidget{background: #F0F0F0;}""")

		self.exercise01()
		self.exercise02()



	def exercise01(self):

		self.lblNum1 = QtWidgets.QLabel(self.tab1)
		self.lblNum1.setGeometry(70, 40, 101, 16)
		self.lblNum1.setText("Ingrese un número: ")

		self.lblNum2 = QtWidgets.QLabel(self.tab1)
		self.lblNum2.setGeometry(70, 70, 101, 16)
		self.lblNum2.setText("Ingrese un número: ")

		self.lblNum3 = QtWidgets.QLabel(self.tab1)
		self.lblNum3.setGeometry(70, 100, 101, 16)
		self.lblNum3.setText("Ingrese un número: ")

		self.txtAmount1 = QtWidgets.QLineEdit(self.tab1)
		self.txtAmount1.setGeometry(180, 40, 113, 20)
		self.txtAmount1.setMaxLength(9)
		self.txtAmount1.setText("0")
		self.txtAmount1.setAlignment(Qt.AlignCenter)

		self.txtAmount2 = QtWidgets.QLineEdit(self.tab1)
		self.txtAmount2.setGeometry(180, 70, 113, 20)
		self.txtAmount2.setMaxLength(9)
		self.txtAmount2.setText("0")
		self.txtAmount2.setAlignment(Qt.AlignCenter)

		self.txtAmount3 = QtWidgets.QLineEdit(self.tab1)
		self.txtAmount3.setGeometry(180, 100, 113, 20)
		self.txtAmount3.setMaxLength(9)
		self.txtAmount3.setText("0")
		self.txtAmount3.setAlignment(Qt.AlignCenter)

		self.btnSort = QtWidgets.QPushButton(self.tab1)
		self.btnSort.setGeometry(320, 60, 91, 41)
		self.btnSort.setText("ORDENAR")
		self.btnSort.setStyleSheet("font-weight: bold;")
		self.btnSort.clicked.connect(self.sort)

		self.lcdNumTop = QtWidgets.QLCDNumber(self.tab1)
		self.lcdNumTop.setGeometry(80, 180, 171, 23)
		self.lcdNumTop.setStyleSheet("background-color: black;")
		self.lcdNumTop.setDigitCount(9)

		self.lcdNumMid = QtWidgets.QLCDNumber(self.tab1)
		self.lcdNumMid.setGeometry(80, 220, 171, 23)
		self.lcdNumMid.setStyleSheet("background-color: black;")
		self.lcdNumMid.setDigitCount(9)

		self.lcdNumBot = QtWidgets.QLCDNumber(self.tab1)
		self.lcdNumBot.setGeometry(80, 260, 171, 23)
		self.lcdNumBot.setStyleSheet("background-color: black;")
		self.lcdNumBot.setDigitCount(9)

		self.lblNumTop = QtWidgets.QLabel(self.tab1)
		self.lblNumTop.setGeometry(270, 180, 101, 16)
		self.lblNumTop.setText("Es el número mayor")

		self.lblNumMid = QtWidgets.QLabel(self.tab1)
		self.lblNumMid.setGeometry(270, 220, 130, 16)
		self.lblNumMid.setText("Es el número intermedio")

		self.lblNumBot = QtWidgets.QLabel(self.tab1)
		self.lblNumBot.setGeometry(270, 260, 101, 16)
		self.lblNumBot.setText("Es el número menor")

	def sort(self):
		a = int(self.txtAmount1.text())
		b = int(self.txtAmount2.text())
		c = int(self.txtAmount3.text())
		self.lcdNumTop.display(maximum(a,b,c))
		if (middle(a,b,c)) == 000:
			self.lblNumMid.setText("No hay número intermedio")
		else:
			self.lblNumMid.setText("Es el número intermedio")
		self.lcdNumMid.display(middle(a,b,c))
		self.lcdNumBot.display(minimum(a,b,c))



	def exercise02(self):

		self.txtNum1 = QtWidgets.QLineEdit(self.tab2)
		self.txtNum1.setGeometry(180, 40, 113, 20)
		self.txtNum1.setMaxLength(9)
		self.txtNum1.setText("0")
		self.txtNum1.setAlignment(Qt.AlignCenter)

		self.txtNum2 = QtWidgets.QLineEdit(self.tab2)
		self.txtNum2.setGeometry(180, 80, 113, 20)
		self.txtNum2.setMaxLength(9)
		self.txtNum2.setText("0")
		self.txtNum2.setAlignment(Qt.AlignCenter)

		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)

		self.btnPlus = QtWidgets.QPushButton(self.tab2)
		self.btnPlus.setGeometry(180, 130, 111, 23)
		self.btnPlus.setFont(font)
		self.btnPlus.setText("Sumar")
		self.btnPlus.clicked.connect(self.add)

		self.btnMinus = QtWidgets.QPushButton(self.tab2)
		self.btnMinus.setGeometry(180, 170, 111, 23)
		self.btnMinus.setFont(font)
		self.btnMinus.setText("Restar")
		self.btnMinus.clicked.connect(self.sub)

		self.btnTimes = QtWidgets.QPushButton(self.tab2)
		self.btnTimes.setGeometry(180, 210, 111, 23)
		self.btnTimes.setFont(font)
		self.btnTimes.setText("Multiplicar")
		self.btnTimes.clicked.connect(self.mul)

		self.btnDivided = QtWidgets.QPushButton(self.tab2)
		self.btnDivided.setGeometry(180, 250, 111, 23)
		self.btnDivided.setFont(font)
		self.btnDivided.setText("Dividir")
		self.btnDivided.clicked.connect(self.div)

		self.btnPow = QtWidgets.QPushButton(self.tab2)
		self.btnPow.setGeometry(180, 290, 111, 23)
		self.btnPow.setFont(font)
		self.btnPow.setText("Potenciar")
		self.btnPow.clicked.connect(self.pow)

	def getValues(self):
		a = int(self.txtNum1.text())
		b = int(self.txtNum2.text())
		return a,b

	def showMessage(self, text):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setText("El resultado es: " + text)
		msgBox.setWindowTitle("Resultado")

		msgBox.exec()

	def add(self):
		a,b = self.getValues()
		self.showMessage(str(addition(a,b)))

	def sub(self):
		a,b = self.getValues()
		self.showMessage(str(subtraction(a,b)))

	def mul(self):
		a,b = self.getValues()
		self.showMessage(str(multiplication(a,b)))

	def div(self):
		a,b = self.getValues()
		self.showMessage(str(division(a,b)))

	def pow(self):
		a,b = self.getValues()
		self.showMessage(str(power(a,b)))