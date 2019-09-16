
import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QDialog, QPushButton, QLabel, QAction, QMessageBox
from PyQt5.QtGui import QIcon

from lab01.index import Exercice01 as lab01exe01

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
		menuLabs = menuBar.addMenu("Laboratorios")

		### ------ Se creará un menu por cada laboratorio, con sus respectivos submenus ------ ###

		menuLabo1 = menuLabs.addMenu("Laboratorio 1")

		actionExe1 = QAction(QIcon(), "Ejercicio 1", self)
		actionExe1.setShortcut("Ctrl+o")
		actionExe1.setStatusTip("Abrir ejercicio 1")
		actionExe1.triggered.connect(self.openIndex01)
		menuLabo1.addAction(actionExe1)

		### ------------------------------------------------------------------------------------ ###


	### Se creará un 'openIndex' por cada laboratorio ###
	def openIndex01(self):
		subwin = lab01exe01(self)
		self.mdiArea.addSubWindow(subwin)
		subwin.setGeometry(20, 50, subwin.x, subwin.y)
		subwin.show()

	### --------------------------------------------- ###

app = QApplication(sys.argv)
window = MainPyQt()
window.show()
app.exec_()
