
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget
from PyQt5 import QtCore, QtGui, QtWidgets

from lab02.exe01 import *

class Index(QTabWidget):
	''' Interfaz que conecta la GUI principal con los ejercicios del laboratorio 2 '''

	x = 690
	y = 210

	def __init__(self, parent=None):
		QTabWidget.__init__(self, parent)
		self.setWindowTitle("Laboratorio 1")

		self.tab1 = QtWidgets.QWidget()
		self.addTab(self.tab1, "Ejercicio 1")
		
		#QTabBar::tab:selected {background: #F0F0F0;}
		self.setStyleSheet("""QTabWidget>QWidget>QWidget{background: #F0F0F0;}""")
		self.exercise01()



	def exercise01(self):

		self.lblUmb1 = QtWidgets.QLabel(self)
		self.lblUmb1.setGeometry(200, 40, 71, 16)
		self.lblUmb1.setText("Primer Umbral")

		self.lblUmb1 = QtWidgets.QLabel(self)
		self.lblUmb1.setGeometry(370, 40, 81, 16)
		self.lblUmb1.setText("Segundo Umbral")

		self.txtUmb1 = QtWidgets.QLineEdit(self)
		self.txtUmb1.setGeometry(180, 60, 113, 20)
		self.txtUmb1.setText("0")

		self.txtUmb2 = QtWidgets.QLineEdit(self)
		self.txtUmb2.setGeometry(350, 60, 113, 20)
		self.txtUmb2.setText("0")

		self.btnIden = QtWidgets.QPushButton(self)
		self.btnIden.setGeometry(30, 110, 75, 31)
		self.btnIden.setText("Identidad")
		self.btnIden.setStyleSheet("font-weight: bold;")
		self.btnIden.clicked.connect(identity)

		self.btnNega = QtWidgets.QPushButton(self)
		self.btnNega.setGeometry(120, 110, 75, 31)
		self.btnNega.setText("Negativo")
		self.btnNega.setStyleSheet("font-weight: bold;")
		self.btnNega.clicked.connect(negative)

		self.btnThres = QtWidgets.QPushButton(self)
		self.btnThres.setGeometry(210, 110, 75, 31)
		self.btnThres.setText("Umbral")
		self.btnThres.setStyleSheet("font-weight: bold;")
		self.btnThres.clicked.connect(self.thres)

		self.btnInverThres = QtWidgets.QPushButton(self)
		self.btnInverThres.setGeometry(300, 110, 101, 31)
		self.btnInverThres.setText("Umbral Inverso")
		self.btnInverThres.setStyleSheet("font-weight: bold;")
		self.btnInverThres.clicked.connect(self.inverThres)

		self.btnDoubleThres = QtWidgets.QPushButton(self)
		self.btnDoubleThres.setGeometry(410, 110, 91, 31)
		self.btnDoubleThres.setText("Doble Umbral")
		self.btnDoubleThres.setStyleSheet("font-weight: bold;")
		self.btnDoubleThres.clicked.connect(self.doubleThres)

		self.btnDoInThres = QtWidgets.QPushButton(self)
		self.btnDoInThres.setGeometry(510, 110, 131, 31)
		self.btnDoInThres.setText("Doble Umbral Inverso")
		self.btnDoInThres.setStyleSheet("font-weight: bold;")
		self.btnDoInThres.clicked.connect(self.doInThres)

	def getValues(self):
		a = int(self.txtUmb1.text())
		b = int(self.txtUmb2.text())
		return a,b

	def showMessage(self, text):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setText(text)
		msgBox.setWindowTitle("Advertencia")

		msgBox.exec()

	def thres(self):
		a,b = self.getValues()
		if a == 0:
			self.showMessage("Se necesita un valor diferente de 0 en el primer umbral")
		else:
			threshold(a)

	def inverThres(self):
		a,b = self.getValues()
		if a == 0:
			self.showMessage("Se necesita un valor diferente de 0 en el primer umbral")
		else:
			inverseThreshold(a)

	def doubleThres(self):
		a,b = self.getValues()
		if a == 0:
			self.showMessage("Se necesita un valor diferente de 0 en el primer umbral")
		elif b == 0:
			self.showMessage("Se necesita un valor diferente de 0 en el segundo umbral")
		else:
			doubleThreshold(a,b)

	def doInThres(self):
		a,b = self.getValues()
		if a == 0:
			self.showMessage("Se necesita un valor diferente de 0 en el primer umbral")
		elif b == 0:
			self.showMessage("Se necesita un valor diferente de 0 en el segundo umbral")
		else:
			doubleInverseThreshold(a,b)