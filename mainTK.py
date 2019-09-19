
from tkinter import *
from lab01.indexTK import IndexTK as Index01
from lab02.indexTK import IndexTK as Index02
from lab03.indexTK import IndexTK as Index03

class MainTK(Frame):
	''' GUI con tkinter principal que llama las demás interfaces en forma de ventanas '''

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack(expand=True)
		self.master.title("LABORATORIOS DE PYTHON")
		self.master.geometry('800x600')
		self.initMenu()

	def initMenu(self):
		menubar = Menu(self.master)
		self.master.config(menu=menubar)


		### Se creará un 'command' por cada laboratorio ###
		labsmenu = Menu(menubar, tearoff=0) # 'tearoff' quita un elemento que aparece por defecto en el menu
		labsmenu.add_command(label="Laboratorio 1", command=self.openIndex01)
		labsmenu.add_command(label="Laboratorio 2", command=self.openIndex02)
		labsmenu.add_command(label="Laboratorio 3", command=self.openIndex03)

		### ------------------------------------------- ###


		menubar.add_cascade(label="Laboratorios", menu=labsmenu)


	### Se creará un 'openIndex' por cada laboratorio ###
	def openIndex01(self):
		window = self.openWindow("Labo1")
		Index01(window)

	def openIndex02(self):
		window = self.openCustomWindow("Labo2",750,400)
		Index02(window)

	def openIndex03(self):
		window = self.openWindow("Labo3")
		Index03(window)

	### --------------------------------------------- ###


	def openWindow(self, ti):
		''' Función que retorna la interfaz Toplevel ya configurada '''
		w = Toplevel(self.master)
		w.title(ti)
		w.geometry("650x400+700+200")
		return w

	def openCustomWindow(self, ti, x, y):
		''' Función que retorna la interfaz Toplevel ya configurada con medidas personalizadas '''
		w = Toplevel(self.master)
		w.title(ti)
		w.geometry(str(x)+"x"+str(y)+"+700+200")
		return w

MainTK().mainloop()