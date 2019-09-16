
import sys
from PyQt5 import Qt, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMdiSubWindow, QLabel, QLineEdit, QPushButton, QLCDNumber, QVBoxLayout, QWidget, QAction, QTabWidget, QVBoxLayout

from lab01.exe01 import *

class Exercice01(QMdiSubWindow):

	x = 500
	y = 400

	def __init__(self, parent=None):
		QMdiSubWindow.__init__(self, parent)

		self.setWindowTitle("Laboratorio 1")

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