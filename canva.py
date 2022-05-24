from tkinter import *
import time

root = Tk()

def one_two(one, two):
    canva.move(one, speed, 0)
    canva.move(two, -speed, 0)
    root.update()
    time.sleep(speed_time)
    if(canva.coords(one)[0] < 3*x + 15):
        one_two(one, two)
    if(canva.coords(two)[0] > x + 30):
        one_two(one, two)

def two_three(two, three):
    canva.move(two, speed, 0)
    canva.move(three, -speed, 0)
    root.update()
    time.sleep(speed_time)
    if(canva.coords(two)[0] < 5*x + 30):
        two_three(two, three)
    if(canva.coords(three)[0] < 3*x + 15):
        two_three(two, three)

def one_three(one, three):
    canva.move(one, speed, 0)
    canva.move(three, -speed, 0)
    root.update()
    time.sleep(speed_time)
    if(canva.coords(one)[0] < 5*x + 30):
        one_three(one, three)
    if(canva.coords(three)[0] > x + 30):
        one_three(one, three)


def move(movements):
    if(movements == "1 2"):
        ...
    elif(movements == "2 3"):
        ...
    elif(movements == "1 3"):
        ...

def start_game(event):
    two_three(item2, item3)
    one_two(item1, item3)
    one_three(item3, item2)




# movimientos: "1 2", "2 3", "1 3"
# desplazamiento: 10, 20, 30, 40, 50
# tiempo: 0.05, 0.04, 0.03, 0.02, 0.015, 0.0145, 0.014, 0.012, 0.01
# carta: J, K, Q
# posicion: I, M, D

# mover(movimientos, desplazamiento, tiempo, carta)
#   return posicion

speed = 50
speed_time = 0.014
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