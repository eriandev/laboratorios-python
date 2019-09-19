''' Operaciones para procesar las imágenes en base al umbral ingresado '''

from PIL import Image

def convertImage():
	imgGray = Image.open("img/machu_picchu.jpg").convert("L")
	x,y = imgGray.size
	return imgGray,x,y

def identity():
	img,width,hight = convertImage()
	output = Image.new("L", (width,hight))
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			p = img.getpixel((i,j))
			q = p #identidad
			output.putpixel((i,j),q)
	output.save("identidad.tif")
	output.show()

def negative():
	img,width,hight = convertImage()
	output = Image.new("L", (width,hight))
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			p = img.getpixel((i,j))
			q = 255 - p #negativo
			output.putpixel((i,j),q)
	output.save("negativo.tif")
	output.show()

def threshold(sill):
	img,width,hight = convertImage()
	output = Image.new("L", (width,hight))
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			p = img.getpixel((i,j))
			if p<=sill: #umbral
				q = 0
			else:
				q = 255
			output.putpixel((i,j),q)
	output.save("umbral.tif")
	output.show()

def inverseThreshold(sill):
	img,width,hight = convertImage()
	output = Image.new("L", (width,hight))
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			p = img.getpixel((i,j))
			if p<=sill: #umbral_inverso
				q = 255
			else:
				q = 0
			output.putpixel((i,j),q)
	output.save("umbral_inverso.tif")
	output.show()

def doubleThreshold(sill1, sill2):
	img,width,hight = convertImage()
	output = Image.new("L", (width,hight))
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			p = img.getpixel((i,j))
			if p<=sill1 and p<=sill2:
				q = 255
			else:
				q = 0
			output.putpixel((i,j),q)
	output.save("doble_umbral.tif")
	output.show()

def doubleInverseThreshold(sill1, sill2):
	img,width,hight = convertImage()
	output = Image.new("L", (width,hight))
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			p = img.getpixel((i,j))
			if p<=sill1 and p<=sill2:
				q = 0
			else:
				q = 255
			output.putpixel((i,j),q)
	output.save("doble_umbral_inverso.tif")
	output.show()