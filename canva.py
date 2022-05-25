import random
from tkinter import *
import time

# ====================================== TKINTER ===================================== #
# ==== MOSTRAR 1 CARTA ===== #

def mostrar_carta(carta):
    ancho_carta = q.width()
    altura_carta = q.height()
    canva = Canvas(width=ancho_carta + 70, height=altura_carta + 20)
    canva.pack()
    x = (ancho_carta)/2.0
    y = (altura_carta)/2.0
    if(carta == "Q"):
        carta = canva.create_image(x + 30, y, image=q)
    elif(carta == "K"):
        carta = canva.create_image(x + 30, y, image=k)
    elif(carta == "J"):
        carta = canva.create_image(x + 30, y, image=j)
    root.after(5000, lambda: root.destroy())

# ===== MOVIMIENTO ===== #

def uno_dos(uno, dos, desplazamiento, tiempo):
    canva.move(uno, desplazamiento, 0)
    canva.move(dos, -desplazamiento, 0)
    root.update()
    time.sleep(tiempo)
    if(canva.coords(uno)[0] < 3*longitud_carta + 15):
        uno_dos(uno, dos, desplazamiento, tiempo)
    if(canva.coords(dos)[0] > longitud_carta + 30):
        uno_dos(uno, dos, desplazamiento, tiempo)


def dos_tres(dos, tres, desplazamiento, tiempo):
    canva.move(dos, desplazamiento, 0)
    canva.move(tres, -desplazamiento, 0)
    root.update()
    time.sleep(tiempo)
    if(canva.coords(dos)[0] < 5*longitud_carta + 30):
        dos_tres(dos, tres, desplazamiento, tiempo)
    if(canva.coords(tres)[0] < 3*longitud_carta + 15):
        dos_tres(dos, tres, desplazamiento, tiempo)


def uno_tres(uno, tres, desplazamiento, tiempo):
    canva.move(uno, desplazamiento, 0)
    canva.move(tres, -desplazamiento, 0)
    root.update()
    time.sleep(tiempo)
    if(canva.coords(uno)[0] < 5*longitud_carta + 30):
        uno_tres(uno, tres, desplazamiento, tiempo)
    if(canva.coords(tres)[0] > longitud_carta + 30):
        uno_tres(uno, tres, desplazamiento, tiempo)


def mover(movements, posicion, desplazamiento, tiempo, tiempo_espera):
    if(movements == "1 2"):
        uno_dos(posicion[0][1], posicion[1][1], desplazamiento, tiempo)

        # actualizar posicion e item
        ans_pos = posicion[0]
        posicion[0] = posicion[1]
        posicion[1] = ans_pos
    elif(movements == "2 3"):
        dos_tres(posicion[1][1], posicion[2][1], desplazamiento, tiempo)

        # actualizar posicion e item
        ans_pos = posicion[1]
        posicion[1] = posicion[2]
        posicion[2] = ans_pos
    elif(movements == "1 3"):
        uno_tres(posicion[0][1], posicion[2][1], desplazamiento, tiempo)

        # actualizar posicion e item
        ans_pos = posicion[0]
        posicion[0] = posicion[2]
        posicion[2] = ans_pos
    time.sleep(tiempo_espera)
    #print(posicion[0][0], posicion[1][0], posicion[2][0])
    return posicion

    

# ===== GENERADORES ===== #

def generar_cartas_visibles():
   
    ancho_carta = q.width()
    altura_carta = q.height()
    canva = Canvas(width=ancho_carta*3 + 70, height=altura_carta + 20)
    canva.pack()
    longitud_carta = (ancho_carta)/2.0
    y = (altura_carta)/2.0
    cards = [["Q", q], ["K", k],["J", j]]
    random.shuffle(cards)
    canva.create_image(longitud_carta + 30, y, image=cards[0][1])
    canva.create_image(3*longitud_carta + 30, y, image=cards[1][1])
    canva.create_image(5*longitud_carta + 30, y, image=cards[2][1])
    root.after(3000, lambda: root.destroy())
    return [[cards[0][0]], [cards[1][0]], [cards[2][0]]]

def generar_cartas_escondidas(posicion):
    global canva
    global longitud_carta
    ancho_carta = carta_escondida.width()
    altura_carta = carta_escondida.height()
    canva = Canvas(width=ancho_carta*3 + 70, height=altura_carta + 20)
    canva.pack()
    longitud_carta = (ancho_carta)/2.0
    y = (altura_carta)/2.0
    item1 = canva.create_image(longitud_carta + 30, y, image=carta_escondida)
    item2 = canva.create_image(3*longitud_carta + 30, y, image=carta_escondida)
    item3 = canva.create_image(5*longitud_carta + 30, y, image=carta_escondida)
    posicion[0].append(item1)
    posicion[1].append(item2)
    posicion[2].append(item3)
    return posicion

# ===== MOVER ===== #

def mover_cartas(posicion, movimientos, desplazamiento, tiempo, carta, tiempo_espera):
    global resultado
    for mov in movimientos:
        posicion = mover(mov, posicion, desplazamiento, tiempo, tiempo_espera)
    root.after(1000, lambda: root.destroy())
    if(posicion[0][0] == carta):
        resultado = "I"
    elif(posicion[1][0] == carta):
        resultado = "M"
    else:
        resultado = "D"


# cartas = ['Q', 'K', 'P']
# mostrar_carta(cartas[random.randint(0,3)])

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
    # tiempo_espera = max(0, tiempo_espera)

root = Tk()

q = PhotoImage(file="./resources/images/q.png")
k = PhotoImage(file="./resources/images/k.png")
j = PhotoImage(file="./resources/images/j.png")

mostrar_carta("Q")
root.mainloop()

root = Tk()

q = PhotoImage(file="./resources/images/q.png")
k = PhotoImage(file="./resources/images/k.png")
j = PhotoImage(file="./resources/images/j.png")

posicion = generar_cartas_visibles()

root.mainloop()

root = Tk()

carta_escondida = PhotoImage(file="./resources/images/card.png")

canva = ""
longitud_carta = 0

resultado = ""

input()


root.after(1000, lambda: mover_cartas(generar_cartas_escondidas(posicion),['1 2', '2 3', '1 3', '1 3', '2 3'], 30, 0.05, 'Q', 0.5))

lista = []
# desplazamiento = 50
# tiempo = 234
carta_interes = 'Q'
# tiempo_espera = 0




root.mainloop()

print(resultado)
