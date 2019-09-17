
import sys
from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMdiSubWindow, QLabel, QLineEdit, QPushButton, QLCDNumber, QWidget, QAction, QMessageBox

from lab01.exe01 import *
from lab01.exe02 import *

class Exercise01(QMdiSubWindow):

	x = 500
	y = 400

	def __init__(self, parent=None):
		QMdiSubWindow.__init__(self, parent)

		self.setWindowTitle("Ejercicio 1")

		self.lblNum1 = QLabel(self)
		self.lblNum1.setGeometry(30, 80, 101, 16)
		self.lblNum1.setText("Ingrese un número: ")

		self.lblNum2 = QLabel(self)
		self.lblNum2.setGeometry(30, 110, 101, 16)
		self.lblNum2.setText("Ingrese un número: ")

		self.lblNum3 = QLabel(self)
		self.lblNum3.setGeometry(30, 140, 101, 16)
		self.lblNum3.setText("Ingrese un número: ")

		self.txtNum1 = QLineEdit(self)
		self.txtNum1.setGeometry(140, 80, 113, 20)
		self.txtNum1.setText("0")

		self.txtNum2 = QLineEdit(self)
		self.txtNum2.setGeometry(140, 110, 113, 20)
		self.txtNum2.setText("0")

		self.txtNum3 = QLineEdit(self)
		self.txtNum3.setGeometry(140, 140, 113, 20)
		self.txtNum3.setText("0")

		self.btnSort = QPushButton(self)
		self.btnSort.setGeometry(280, 100, 91, 41)
		self.btnSort.setText("ORDENAR")
		self.btnSort.setStyleSheet("font-weight: bold;")
		self.btnSort.clicked.connect(self.sort)

		self.lcdNumTop = QLCDNumber(self)
		self.lcdNumTop.setGeometry(40, 220, 171, 23)
		self.lcdNumTop.setStyleSheet("""QLCDNumber {background-color: black;}""")

		self.lcdNumMid = QLCDNumber(self)
		self.lcdNumMid.setGeometry(40, 260, 171, 23)
		self.lcdNumMid.setStyleSheet("""QLCDNumber {background-color: black;}""")

		self.lcdNumBot = QLCDNumber(self)
		self.lcdNumBot.setGeometry(40, 300, 171, 23)
		self.lcdNumBot.setStyleSheet("""QLCDNumber {background-color: black;}""")

		self.lblNumTop = QLabel(self)
		self.lblNumTop.setGeometry(230, 220, 101, 16)
		self.lblNumTop.setText("Es el número mayor")

		self.lblNumMid = QLabel(self)
		self.lblNumMid.setGeometry(230, 260, 130, 16)
		self.lblNumMid.setText("Es el número intermedio")

		self.lblNumBot = QLabel(self)
		self.lblNumBot.setGeometry(230, 300, 101, 16)
		self.lblNumBot.setText("Es el número menor")

	def sort(self):
		a = int(self.txtNum1.text())
		b = int(self.txtNum2.text())
		c = int(self.txtNum3.text())
		self.lcdNumTop.display(maximum(a,b,c))
		if (middle(a,b,c)) == 000:
			self.lblNumMid.setText("No hay número intermedio")
		else:
			self.lblNumMid.setText("Es el número intermedio")
		self.lcdNumMid.display(middle(a,b,c))
		self.lcdNumBot.display(minimum(a,b,c))



class Exercise02(QMdiSubWindow):

	x = 230
	y = 350

	def __init__(self, parent=None):
		QMdiSubWindow.__init__(self, parent)

		self.setWindowTitle("Ejercicio 2")

		self.txtNum1 = QLineEdit(self)
		self.txtNum1.setGeometry(60, 40, 113, 20)
		self.txtNum1.setText("0")

		self.txtNum2 = QLineEdit(self)
		self.txtNum2.setGeometry(60, 80, 113, 20)
		self.txtNum2.setText("0")

		font = QtGui.QFont()
		font.setBold(True)
		font.setWeight(75)

		self.btnPlus = QPushButton(self)
		self.btnPlus.setGeometry(60, 130, 111, 23)
		self.btnPlus.setFont(font)
		self.btnPlus.setText("Sumar")
		self.btnPlus.clicked.connect(self.add)

		self.btnMinus = QPushButton(self)
		self.btnMinus.setGeometry(60, 170, 111, 23)
		self.btnMinus.setFont(font)
		self.btnMinus.setText("Restar")
		self.btnMinus.clicked.connect(self.sub)

		self.btnTimes = QPushButton(self)
		self.btnTimes.setGeometry(60, 210, 111, 23)
		self.btnTimes.setFont(font)
		self.btnTimes.setText("Multiplicar")
		self.btnTimes.clicked.connect(self.mul)

		self.btnDivided = QPushButton(self)
		self.btnDivided.setGeometry(60, 250, 111, 23)
		self.btnDivided.setFont(font)
		self.btnDivided.setText("Dividir")
		self.btnDivided.clicked.connect(self.div)

		self.btnPow = QPushButton(self)
		self.btnPow.setGeometry(60, 290, 111, 23)
		self.btnPow.setFont(font)
		self.btnPow.setText("Potenciar")
		self.btnPow.clicked.connect(self.pow)

	def getValues(self):
		a = int(self.txtNum1.text())
		b = int(self.txtNum2.text())
		return a,b

	def showMessage(self, text):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
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