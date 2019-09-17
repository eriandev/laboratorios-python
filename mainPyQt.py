
import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QDialog, QPushButton, QLabel, QAction, QMessageBox
from PyQt5.QtGui import QIcon

from lab01.index import Exercise01 as lab01exe01
from lab01.index import Exercise02 as lab01exe02

class MainPyQt(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.resize(800,600)
		self.setWindowTitle("LABORATORIOS PYTHON")
		self.statusBar().showMessage('Mensaje de bienvenida')

		self.mdiArea = QtWidgets.QMdiArea(self)
		self.mdiArea.setGeometry(0, 0, 800, 599)

		self.initMenuBar()

	def initMenuBar(self):
		menuBar = self.menuBar()

		### ------ Se creará un menu por cada laboratorio, con sus respectivos actions ------ ###

		menuLab01 = menuBar.addMenu("Laboratorio I")

		actLab01Exe01 = QAction(QIcon(), "Ejercicio 1", self)
		#actLab01Exe01.setShortcut("Ctrl+o")
		actLab01Exe01.setStatusTip("Abrir ejercicio 1")
		actLab01Exe01.triggered.connect(self.openLab01Exe01)
		menuLab01.addAction(actLab01Exe01)

		actLab01Exe01 = QAction(QIcon(), "Ejercicio 2", self)
		actLab01Exe01.setStatusTip("Abrir ejercicio 2")
		actLab01Exe01.triggered.connect(self.openLab01Exe02)
		menuLab01.addAction(actLab01Exe01)

		### ------------------------------------------------------------------------------------ ###


	### Se creará un 'openLab' por cada ejercicio de cada laboratorio ###
	def openLab01Exe01(self):
		subwin = lab01exe01(self)
		self.mdiArea.addSubWindow(subwin)
		subwin.setGeometry(20, 50, subwin.x, subwin.y)
		subwin.show()

	def openLab01Exe02(self):
		subwin = lab01exe02(self)
		self.mdiArea.addSubWindow(subwin)
		subwin.setGeometry(20, 50, subwin.x, subwin.y)
		subwin.show()

	### --------------------------------------------- ###

app = QApplication(sys.argv)
window = MainPyQt()
window.show()
app.exec_()
