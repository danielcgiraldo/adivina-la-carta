from tkinter import *
import time

root = Tk()

def l_m(item):
    canva.move(item, 100, 0)
    root.update()
    time.sleep(0.05)
    if(canva.coords(item)[0] < 3*x + 15):
        l_m(item)
        root.update()

def l(item):
    canva.move(item, -100, 0)
    root.update()
    time.sleep(0.05)
    if(canva.coords(item)[0] > x + 30):
        l(item)

def r(item):
    canva.move(item, 100, 0)
    root.update()
    time.sleep(0.05)
    if(canva.coords(item)[0] < 5*x + 30):
        r(item)

def start_game(event):
    r(item1)
    l(item3)
    l(item2)
    l_m(item3)

photo1 = PhotoImage(file="./resources/images/card.png")
width1 = photo1.width()
height1 = photo1.height()
canva = Canvas(width=width1*3 + 70, height=height1 + 20)
canva.pack()
x = (width1)/2.0
y = (height1)/2.0
item1 = canva.create_image(x + 30, y, image=photo1)
item2 = canva.create_image(3*x + 30, y, image=photo1)
item3 = canva.create_image(5*x + 30, y, image=photo1)
canva.bind('<Button-1>', start_game)


root.mainloop() 