# Importing Image from PIL package
from sys import stdout
import math
from PIL import Image
density = 'Ñ@#W$9876543210?!abc;:+=-,._ '
i = 0
p = 0
# creating a image object
im = Image.open(r"C:\leave.jpg")#File name go here
coordinate = x, y = 150, 59
# using getpixel method
while i < im.height:
    while p <im.width:
        coordinate = x, y = p, i
        print(density[math.floor((sum(im.getpixel(coordinate))/27.32))],end=" ")
        p+=1
    i += 1
    print()
    p = 0

    

