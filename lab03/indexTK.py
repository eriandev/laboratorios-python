
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from lab03.exe01 import *

class IndexTK(Frame):
	''' Sirve de index entre la GUI tkinter principal y los ejercicios del laboratorio 3 '''

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.initNotebook()
		self.pack()

	def initNotebook(self):
		notebook = ttk.Notebook(self.master)
		notebook.pack(fill='both', expand='yes')
		tab1 = ttk.Frame(notebook)
		notebook.add(tab1, text='Ejercicio 1')
		self.exercise01(tab1)
		notebook.pack()



	## -- Ejercicio 1 -- ##
	def exercise01(self, tab):

		lblnum1 = Label(tab, text="Elegir una opción: ")
		lblnum1.grid(column=2, row=1)

		def roberts():
			selectFilter(1)

		def prewit():
			selectFilter(2)

		def sobel():
			selectFilter(3)

		def average():
			selectFilter(4)

		btnaverage = Button(tab, text="Usar Promedio", bg="green", fg="white", command=average)
		btnaverage.grid(column=3, row=2)

		btnroberts = Button(tab, text="Usar Roberts", bg="green", fg="white", command=roberts)
		btnroberts.grid(column=4, row=2)

		btnprewit = Button(tab, text="Usar Prewit", bg="green", fg="white", command=prewit)
		btnprewit.grid(column=5, row=2)

		btnsobel = Button(tab, text="Usar Sobel", bg="green", fg="white", command=sobel)
		btnsobel.grid(column=6, row=2)