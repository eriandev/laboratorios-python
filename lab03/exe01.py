from PIL import Image
import math

imgGray = Image.open("img/machu_picchu.jpg").convert("L")
weight, height = imgGray.size

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

average = [ [0.1,0.1,0.1],
             [0.1,0.1,0.1],
             [0.1,0.1,0.1]]

def selectFilter(option):
    if option == 1:
        result = setCustomFilter(imgGray, robertsX, robertsY)
        result.save("img/roberts.tif")
        result.show()

    elif option==2:
        result = setCustomFilter(imgGray, prewittX, prewittY)
        result.save("img/prewitt.tif")
        result.show()
        
    elif option==3:
        result = setCustomFilter(imgGray, sobelX, sobelY)
        result.save("img/sobel.tif")
        result.show()

    elif option==4:
        result = setAverageFilter(imgGray, average)
        result.save("img/promedio.tif")
        result.show()
    
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