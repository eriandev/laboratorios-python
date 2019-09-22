
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from lab01.index import Index as lab01
from lab02.index import Index as lab02
from lab03.index import Index as lab03

class MainPyQt(QMainWindow):
	''' GUI principal con PyQt5 que llama las demás subventanas '''

	def __init__(self):
		QMainWindow.__init__(self)
		self.resize(1280,720)
		self.setWindowTitle("Laboratorios Python")
		self.statusBar().showMessage('Mensaje de bienvenida')

		self.mdiArea = QtWidgets.QMdiArea(self)
		self.mdiArea.setGeometry(0, 0, 1000, 650)

		self.setCentralWidget(self.mdiArea)

		self.initMenuBar()

	def initMenuBar(self):

		menuBar = self.menuBar()

		self.actCloseAll = QtWidgets.QAction(
			"", self, statusTip="", triggered=self.mdiArea.closeAllSubWindows
		)
		self.actCloseAll.setShortcut("Ctrl+x")
		menuBar.addAction(self.actCloseAll)

	#-#-#-#-#-#-# Se creará un action por cada laboratorio #-#-#-#-#-#-#-#-#-#

		actLab01 = QtWidgets.QAction(QtGui.QIcon(), "Laboratorio I", self)
		actLab01.setShortcut("Ctrl+1")
		actLab01.setStatusTip("Abrir laboratorio 1")
		actLab01.triggered.connect(self.openLab01)
		menuBar.addAction(actLab01)

		###------------------------------------------------###

		actLab02 = QtWidgets.QAction(QtGui.QIcon(), "Laboratorio II", self)
		actLab02.setShortcut("Ctrl+2")
		actLab02.setStatusTip("Abrir laboratorio 2")
		actLab02.triggered.connect(self.openLab02)
		menuBar.addAction(actLab02)

		###------------------------------------------------###

		actLab03 = QtWidgets.QAction(QtGui.QIcon(), "Laboratorio III", self)
		actLab03.setShortcut("Ctrl+3")
		actLab03.setStatusTip("Abrir laboratorio 3")
		actLab03.triggered.connect(self.openLab03)
		menuBar.addAction(actLab03)

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



	#-#-#-#-#-#-# Se creará un 'openLab' por cada laboratorio #-#-#-#-#-#-#-#-#
	
	def openLab01(self):
		tabwid = lab01(self)
		subwin = self.mdiArea.addSubWindow(tabwid)
		subwin.setGeometry(30, 30, tabwid.x, tabwid.y)
		subwin.setFixedSize(subwin.size())
		subwin.setWindowFlags(subwin.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
		subwin.show()

	###---------------------------------------------###

	def openLab02(self):
		tabwid = lab02(self)
		subwin = self.mdiArea.addSubWindow(tabwid)
		subwin.setGeometry(30, 30, tabwid.x, tabwid.y)
		subwin.setFixedSize(subwin.size())
		subwin.setWindowFlags(subwin.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
		subwin.show()

	###---------------------------------------------###

	def openLab03(self):
		tabwid = lab03(self)
		subwin = self.mdiArea.addSubWindow(tabwid)
		subwin.setGeometry(30, 30, tabwid.x, tabwid.y)
		subwin.setFixedSize(subwin.size())
		subwin.setWindowFlags(subwin.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
		subwin.show()

	#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#



app = QApplication(sys.argv)
window = MainPyQt()
window.show()
app.exec_()