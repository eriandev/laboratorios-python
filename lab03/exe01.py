''' Operaciones para la extracción de características de imágenes digitales en base al operador seleccionado '''

import math
from PIL import Image
from tkinter import messagebox
from os import listdir, remove, path

imgGray = Image.open("img/machu_picchu.jpg").convert("L")
weight, height = imgGray.size

average = [ [0.1,0.1,0.1],
             [0.1,0.1,0.1],
             [0.1,0.1,0.1]]

robertsX = [ [0.0,0.0,0.0],
             [0.0,1.0,0.0],
             [0.0,0.0,-1.0]]

robertsY = [ [0.0,0.0,0.0],
             [0.0,0.0,1.0],
             [0.0,-1.0,0.0]]

prewittX = [ [-1.0,0.0,1.0],
             [-1.0,0.0,1.0],
             [-1.0,0.0,1.0]]

prewittY = [ [-1.0,-1.0,-1.0],
             [0.0,0.0,0.0],
             [1.0,1.0,1.0]]

sobelX = [ [-1.0,0.0,1.0],
             [-2.0,0.0,2.0],
             [-1.0,0.0,1.0]]

sobelY = [ [-1.0,-2.0,-1.0],
             [0.0,0.0,0.0],
             [1.0,2.0,1.0]]

def openImage(img):
    f = Image.open(img)
    f.show()

def selectFilter(option, visualize=True):
    if option == 1:
        if path.exists("img/promedio.tif"):
            if visualize:
                openImage("img/promedio.tif")
        else:
            result = setAverageFilter(imgGray, average)
            result.save("img/promedio.tif")
            if visualize:
                openImage("img/promedio.tif")

    elif option==2:
        if path.exists("img/roberts.tif"):
            if visualize:
                openImage("img/roberts.tif")
        else:
            result = setCustomFilter(imgGray, robertsX, robertsY)
            result.save("img/roberts.tif")
            if visualize:
                openImage("img/roberts.tif")
        
    elif option==3:
        if path.exists("img/prewitt.tif"):
            if visualize:
                openImage("img/prewitt.tif")
        else:
            result = setCustomFilter(imgGray, prewittX, prewittY)
            result.save("img/prewitt.tif")
            if visualize:
                openImage("img/prewitt.tif")

    elif option==4:
        if path.exists("img/sobel.tif"):
            if visualize:
                openImage("img/sobel.tif")
        else:
            result = setCustomFilter(imgGray, sobelX, sobelY)
            result.save("img/sobel.tif")
            if visualize:
                openImage("img/sobel.tif")

def setAverageFilter(img, M):
    output = Image.new("L",(weight, height))

    Ma,Mb,Mc = M[0][0],M[0][1],M[0][2]
    Md,Me,Mf = M[1][0],M[1][1],M[1][2]
    Mg,Mh,Mi = M[2][0],M[2][1],M[2][2]

    for i in range(2, weight-1):
        for j in range(2, height-1):
            Ia = float(img.getpixel((i-1,j-1)))
            Ib = float(img.getpixel((i-1,j)))
            Ic = float(img.getpixel((i-1,j+1)))
            Id = float(img.getpixel((i,j-1)))
            Ie = float(img.getpixel((i,j)))
            If = float(img.getpixel((i,j+1)))
            Ig = float(img.getpixel((i+1,j-1)))
            Ih = float(img.getpixel((i+1,j)))
            Ii = float(img.getpixel((i+1,j+1)))

            q = int(Ma*Ia+Mb*Ib+Mc*Ic+Md*Id+Me*Ie+Mf*If+Mg*Ig+Mh*Ih+Mi*Ii)

            output.putpixel((i,j),q)
    return output
    
def setCustomFilter(img,H,V):
    output = Image.new("L", (weight, height))

    Ha,Hb,Hc = H[0][0],H[0][1],H[0][2]
    Hd,He,Hf = H[1][0],H[1][1],H[1][2]
    Hg,Hh,Hi = H[2][0],H[2][1],H[2][2]
    Va,Vb,Vc = V[0][0],V[0][1],V[0][2]
    Vd,Ve,Vf = V[1][0],V[1][1],V[1][2]
    Vg,Vh,Vi = V[2][0],V[2][1],V[2][2]
    
    for i in range(2,weight-1):
        for j in range(2,height-1):
            Ia = float(img.getpixel((i-1,j-1)))
            Ib = float(img.getpixel((i-1,j)))
            Ic = float(img.getpixel((i-1,j+1)))
            Id = float(img.getpixel((i,j-1)))
            Ie = float(img.getpixel((i,j)))
            If = float(img.getpixel((i,j+1)))
            Ig = float(img.getpixel((i+1,j-1)))
            Ih = float(img.getpixel((i+1,j)))
            Ii = float(img.getpixel((i+1,j+1)))
            Gx = Ha*Ia+Hb*Ib+Hc*Ic+Hd*Id+He*Ie+Hf*If+Hg*Ig+Hh*Ih+Hi*Ii
            Gy = Va*Ia+Vb*Ib+Vc*Ic+Vd*Id+Ve*Ie+Vf*If+Vg*Ig+Vh*Ih+Vi*Ii

            q = int(math.sqrt(Gx*Gx+Gy*Gy))

            output.putpixel((i,j),q)
    return output

def deleteImages():
    # Para carpetas vacías 'rmdir("carpeta_vacia")'
    # Para carpetas, sus archivos y subcarpetas:
    #   from shutil import rmtree
    #   rmtree("carpeta")

    filelist = [ f for f in listdir("img/") if f.endswith(".tif") ]
    for f in filelist:
        remove("img/"+f)