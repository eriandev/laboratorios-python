
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lab01.exe01 import *
from lab01.exe02 import *

class IndexTK(Frame):
	''' Sirve de index entre la GUI tkinter principal y los ejercicios del laboratorio '''

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
		notebook.add(tab2, text='Ejercicio 2')
		self.exercice01(tab1)
		self.exercice02(tab2)
		notebook.pack()



	## -- Ejercicio 1 -- ##
	def exercice01(self, tab):
		numtop = StringVar() 
		nummid = StringVar()
		numbot = StringVar()
		num1 = IntVar()
		num2 = IntVar()
		num3 = IntVar()

		lblnum1 = Label(tab, text="Ingresar número: ")
		lblnum1.grid(column=1, row=1)
		lblnum2 = Label(tab, text="Ingresar número: ")
		lblnum2.grid(column=1, row=2)
		lblnum3 = Label(tab, text="Ingresar número: ")
		lblnum3.grid(column=1, row=3)

		txtnum1 = Entry(tab, textvariable=num1)
		txtnum1.grid(column=2, row=1)
		txtnum2 = Entry(tab, textvariable=num2)
		txtnum2.grid(column=2, row=2)
		txtnum3 = Entry(tab, textvariable=num3)
		txtnum3.grid(column=2, row=3)

		lbltop = Label(tab, textvariable=numtop)
		lbltop.grid(column=1, row=10)
		lblmid = Label(tab, textvariable=nummid)
		lblmid.grid(column=1, row=11)
		lblbot = Label(tab, textvariable=numbot)
		lblbot.grid(column=1, row=12)

		def sort():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			c = int(txtnum3.get())
			numtop.set("El mayor número es: " + str(top(a,b,c)))
			nummid.set("El número intermedio es: " + str(mid(a,b,c)))
			numbot.set("El menor número es: " + str(bot(a,b,c)))

		btnsort = Button(tab, text="Ordenar", bg="green", fg="white", command=sort)
		btnsort.grid(column=3, row=2)



	## -- Ejercicio 2 -- ##
	def exercice02(self, tab):
		num1 = IntVar()
		num2 = IntVar()

		lblnum1 = Label(tab, text="Ingresar número: ")
		lblnum1.grid(column=0, row=0)
		lblnum2 = Label(tab, text="Ingresar número: ")
		lblnum2.grid(column=0, row=1)

		txtnum1 = Entry(tab, textvariable=num1)
		txtnum1.grid(column=1, row=0)
		txtnum2 = Entry(tab, textvariable=num2)
		txtnum2.grid(column=1, row=1)

		def addition():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			messagebox.showinfo('Suma', add(a,b))

		def subtraction():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			messagebox.showinfo('Resta', sub(a,b))

		def multiplication():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			messagebox.showinfo('Multiplicación', mul(a,b))

		def division():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			messagebox.showinfo('División', div(a,b))

		def power():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			messagebox.showinfo('Potenciación', pow(a,b))

		btnaddition = Button(tab, text="Sumar", bg="green", fg="white", command=addition)
		btnaddition.grid(column=2, row=2)

		btnresta = Button(tab, text="Restar", bg="green", fg="white", command=subtraction)
		btnresta.grid(column=3, row=2)

		btnmulti = Button(tab, text="Multiplicar", bg="green", fg="white", command=multiplication)
		btnmulti.grid(column=4, row=2)

		btnpoten = Button(tab, text="Dividir", bg="green", fg="white", command=division)
		btnpoten.grid(column=5, row=2)

		btnpoten = Button(tab, text="Potenciar", bg="green", fg="white", command=power)
		btnpoten.grid(column=6, row=2)