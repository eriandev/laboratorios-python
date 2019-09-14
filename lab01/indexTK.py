
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from lab01.exe01 import *
from lab01.exe02 import *

class IndexTK(Frame):
	''' Sirve de index entre la GUI tkinter principal y los ejercicios del laboratorio 1'''

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
			numtop.set("El mayor número es: " + str(maximum(a,b,c)))
			nummid.set("El número intermedio es: " + str(middle(a,b,c)))
			numbot.set("El menor número es: " + str(minimum(a,b,c)))

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

		def getValues():
			a = int(txtnum1.get())
			b = int(txtnum2.get())
			return a,b

		def add():
			a,b = getValues()
			messagebox.showinfo('Suma', addition(a,b))

		def sub():
			a,b = getValues()
			messagebox.showinfo('Resta', subtraction(a,b))

		def mul():
			a,b = getValues()
			messagebox.showinfo('Multiplicación', multiplication(a,b))

		def div():
			a,b = getValues()
			messagebox.showinfo('División', division(a,b))

		def pow():
			a,b = getValues()
			messagebox.showinfo('Potenciación', power(a,b))

		btnadd = Button(tab, text="Sumar", bg="green", fg="white", command=add)
		btnadd.grid(column=2, row=2)

		btnsub = Button(tab, text="Restar", bg="green", fg="white", command=sub)
		btnsub.grid(column=3, row=2)

		btnmul = Button(tab, text="Multiplicar", bg="green", fg="white", command=mul)
		btnmul.grid(column=4, row=2)

		btndiv = Button(tab, text="Dividir", bg="green", fg="white", command=div)
		btndiv.grid(column=5, row=2)

		btnpow = Button(tab, text="Potenciar", bg="green", fg="white", command=pow)
		btnpow.grid(column=6, row=2)