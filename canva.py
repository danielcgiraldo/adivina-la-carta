import random
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


def start_game():
    two_three(item2, item3)
    time.sleep(tiempo_espera)
    one_two(item1, item3)
    time.sleep(tiempo_espera)
    one_three(item3, item2)
    root.after(1000, lambda: root.destroy())


def generar_cartas(Q, K, J):
    
    width_card = q.width()
    height_card = q.height()
    canva = Canvas(width=width_card*3 + 70, height=height_card + 20)
    canva.pack()
    x = (width_card)/2.0
    y = (height_card)/2.0
    cards = [["Q", Q], ["K", K],["J", J]]
    random.shuffle(cards)
    left = canva.create_image(x + 30, y, image=cards[0][1])
    middle = canva.create_image(3*x + 30, y, image=cards[1][1])
    right = canva.create_image(5*x + 30, y, image=cards[2][1])
    root.after(5000, lambda: root.destroy())
    return [cards[0][0], cards[1][0], cards[2][0]]

def mover_cartas(movimientos, desplazamiento, tiempo, carta, tiempo_espera):
    posicion = generar_cartas()


# movimientos: "1 2", "2 3", "1 3"
# desplazamiento: 10, 20, 30, 40, 50
# tiempo: 0.05, 0.04, 0.03, 0.02, 0.015, 0.0145, 0.014, 0.012, 0.01
# carta: J, K, Q
# posicion: I, M, D
#tiempo_espera: 0.5, 0.4, 0.3, 0.2, 0.1, 0

# mover(movimientos, desplazamiento, tiempo, carta, tiempo_espera)
#   return posicion


# if(nivel < 5)
    #desplazamiento(10 * nivel)
    #tiempo = 0.05
    #tiempo_espera = 0.5
#   else
    # desplazamiento = 50
    # tiempo = 0.05 - 0.005 * (nivel - 5)
    # tiempo_espera = 0.5 - 0.1 * (nivel - 5)

speed = 10
speed_time = 0.05
tiempo_espera = 0.5
q = PhotoImage(file="./resources/images/q.png")
k = PhotoImage(file="./resources/images/k.png")
j = PhotoImage(file="./resources/images/j.png")
print(generar_cartas(q, k, j))
root.mainloop()
root = Tk()
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
root.after(2000, lambda: start_game())



root.mainloop()