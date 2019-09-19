
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
		tab2 = ttk.Frame(notebook)
		notebook.add(tab1, text='Ejercicio 1')
		notebook.add(tab2, text='Tarea 1')
		self.exercise01(tab1)
		self.homework01(tab2)
		notebook.pack()

		global frame
		frame = Frame(tab2, width=805, height=540, background='white')
		frame.grid(column=3, row=7)
		load = Image.open("img/machu_picchu.jpg")
		render = ImageTk.PhotoImage(load)

		imgF = Label(frame, image=render)
		imgF.image = render
		imgF.place(x=0, y=0)

	def imgFrame(self, img):
		load = Image.open(img)
		render = ImageTk.PhotoImage(load)

		imgF = Label(frame, image=render)
		imgF.image = render
		imgF.place(x=0, y=0)



	## -- Ejercicio 1 -- ##
	def exercise01(self, tab):

		lblnum1 = Label(tab, text="Elegir una opción: ")
		lblnum1.grid(column=2, row=1)

		def average():
			selectFilter(1)

		def roberts():
			selectFilter(2)

		def prewit():
			selectFilter(3)

		def sobel():
			selectFilter(4)

		btnaverage = Button(tab, text="Usar Promedio", bg="green", fg="white", command=average)
		btnaverage.grid(column=3, row=2)

		btnroberts = Button(tab, text="Usar Roberts", bg="green", fg="white", command=roberts)
		btnroberts.grid(column=4, row=2)

		btndelete = Button(tab, text="BORRAR", bg="red", fg="black", command=deleteImages)
		btndelete.grid(column=5, row=3)

		btnprewit = Button(tab, text="Usar Prewit", bg="green", fg="white", command=prewit)
		btnprewit.grid(column=6, row=2)

		btnsobel = Button(tab, text="Usar Sobel", bg="green", fg="white", command=sobel)
		btnsobel.grid(column=7, row=2)




	## -- Tarea 1 -- ##
	def homework01(self, tab):

		def imgAverage():
			selectFilter(1, False)
			self.imgFrame("img/promedio.tif")

		def imgRoberts():
			selectFilter(2, False)
			self.imgFrame("img/roberts.tif")

		def imgPrewit():
			selectFilter(3, False)
			self.imgFrame("img/prewitt.tif")

		def imgSobel():
			selectFilter(4, False)
			self.imgFrame("img/sobel.tif")

		btnimgAverage = Button(tab, text="Usar Promedio", bg="green", fg="white", command=imgAverage)
		btnimgAverage.grid(column=2, row=2)

		btnimgRoberts = Button(tab, text="Usar Roberts", bg="green", fg="white", command=imgRoberts)
		btnimgRoberts.grid(column=2, row=3)

		btnimgPrewit = Button(tab, text="Usar Prewit", bg="green", fg="white", command=imgPrewit)
		btnimgPrewit.grid(column=2, row=4)

		btnimgSobel = Button(tab, text="Usar Sobel", bg="green", fg="white", command=imgSobel)
		btnimgSobel.grid(column=2, row=5)

		btndelete = Button(tab, text="BORRAR", bg="red", fg="black", command=deleteImages)
		btndelete.grid(column=2, row=6)