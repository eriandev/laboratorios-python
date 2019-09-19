
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lab02.exe01 import *

class IndexTK(Frame):
	''' Sirve de index entre la GUI tkinter principal y los ejercicios del laboratorio 2 '''

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
		self.exercise01(tab1)
		notebook.pack()



	## -- Ejercicio 1 -- ##
	def exercise01(self, tab):
		sill1 = IntVar()
		sill2 = IntVar()

		lblsill1 = Label(tab, text="Primer umbral: ")
		lblsill1.grid(column=1, row=1)
		lblsill2 = Label(tab, text="Segundo umbral: ")
		lblsill2.grid(column=1, row=2)

		txtsill1 = Entry(tab, textvariable=sill1)
		txtsill1.grid(column=2, row=1)
		txtsill2 = Entry(tab, textvariable=sill2)
		txtsill2.grid(column=2, row=2)

		def getValues():
			a = int(txtsill1.get())
			b = int(txtsill2.get())
			return a,b

		def iden():
			identity()

		def nega():
			negative()

		def thres():
			a,b = getValues()
			if a == 0:
				messagebox.showinfo('Información requerida', "Se necesita un valor diferente de '0' en 'Primer umbral'")
			else:
				threshold(a)

		def inverThres():
			a,b = getValues()
			if a == 0:
				messagebox.showinfo('Información requerida', "Se necesita un valor diferente de '0' en 'Primer umbral'")
			else:
				inverseThreshold(a)

		def doubleThres():
			a,b = getValues()
			if a == 0:
				messagebox.showinfo('Información requerida', "Se necesita un valor diferente de '0' en 'Primer umbral'")
			elif b == 0:
				messagebox.showinfo('Información requerida', "Se necesita un valor diferente de '0' en 'Segundo umbral'")
			else:
				doubleThreshold(a, b)

		def doInThres():
			a,b = getValues()
			if a == 0:
				messagebox.showinfo('Información requerida', "Se necesita un valor diferente de '0' en 'Primer umbral'")
			elif b == 0:
				messagebox.showinfo('Información requerida', "Se necesita un valor diferente de '0' en 'Segundo umbral'")
			else:
				doubleInverseThreshold(a, b)

		btniden = Button(tab, text="Identidad", bg="green", fg="white", command=iden)
		btniden.grid(column=3, row=3)

		btnnega = Button(tab, text="Negativo", bg="green", fg="white", command=nega)
		btnnega.grid(column=4, row=3)

		btnthres = Button(tab, text="Umbral", bg="green", fg="white", command=thres)
		btnthres.grid(column=5, row=3)

		btninverThres = Button(tab, text="Umbral Inverso", bg="green", fg="white", command=inverThres)
		btninverThres.grid(column=6, row=3)

		btndoubleThres = Button(tab, text="Doble Umbral", bg="green", fg="white", command=doubleThres)
		btndoubleThres.grid(column=7, row=3)

		btndoInThres = Button(tab, text="Doble Umbral Inverso", bg="green", fg="white", command=doInThres)
		btndoInThres.grid(column=8, row=3)