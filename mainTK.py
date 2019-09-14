
from tkinter import *
from lab01.indexTK import IndexTK as Index01

class MainTK(Frame):
	''' GUI con tkinter principal que llama las demás interfaces en forma de ventanas '''

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack(expand=True)
		self.master.title("Ventana Principal")
		self.master.geometry('800x600')
		self.initMenu()

	def initMenu(self):
		menubar = Menu(self.master)
		self.master.config(menu=menubar)


		### Se creará un 'command' por cada laboratorio ###
		labsmenu = Menu(menubar, tearoff=0) # 'tearoff' quita un elemento que aparece por defecto en el menu
		labsmenu.add_command(label="Laboratorio 1", command=self.openIndex01)


		### ------------------------------------------- ###


		menubar.add_cascade(label="Laboratorios", menu=labsmenu)


	### Se creará un 'openIndex' por cada laboratorio ###
	def openIndex01(self):
		window = self.openWindow("Labo1")
		Index01(window)


	### --------------------------------------------- ###


	def openWindow(self, ti):
		''' Función que retorna la interfaz Toplevel ya configurada '''
		w = Toplevel(self.master)
		w.title(ti)
		w.geometry("600x400")
		return w

MainTK().mainloop()