import random
from tkinter import *
import time
from datetime import datetime
from tabulate import tabulate
# ================================================== FUNCIONES ============================================ #

# ============================== PUNTAJES ================================== #

def archivo_leer():
    archivo=open("./resources/db.txt","r")
    tabla=[]
    for renglon in archivo:
        palabra=renglon.split("|")
        tabla.append(palabra)
    archivo.close()
    return tabla

    
def archivo_escribir(tabla):
    archivo=open("./resources/db.txt","w")
    lista=[]
    for i in range(0,len(tabla)):
        renglon1=f"{tabla[i][0]}|{tabla[i][1]}|{int(tabla[i][2])}"
        lista.append(renglon1)
    for renglon in lista:
        print(renglon, end='\n', file=archivo)
    archivo.close()


def definir_puntaje(puntaje, usuario):
    tabla = archivo_leer()
    if(len(tabla) > 0):
        for i in range(0, max(5, len(tabla))):
            if(i > len(tabla) - 1):
                tabla.append([datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), usuario, puntaje])
                break
            else:
                if puntaje > int(tabla[i][2]):
                    tabla.insert(i, [datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), usuario, puntaje])
                elif puntaje == int(tabla[i][2]):
                    tabla.insert(i + 1, [datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), usuario, puntaje])
        if(len(tabla) > 5):
            archivo_escribir(tabla[0:5:1])
        else:
            archivo_escribir(tabla)
    else:
        archivo_escribir([[datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), usuario, puntaje]])


# ========================= ALEATORIO ============================= #

def mostrar_cartas(lista):
    p=lista[random.randint(0,2)]
    return p


def niveles(nivel):
    global desplazamiento
    global tiempo
    global tiempo_espera
    if nivel<5:
        desplazamiento=10*nivel
        tiempo = 0.045
        tiempo_espera = 0.5
    else:
        desplazamiento = 50
        tiempo = 0.045 - 0.005 * (nivel - 5)
        tiempo_espera = 0.5 - 0.1 * (nivel - 5)
        tiempo_espera = max(0, tiempo_espera)

def cambios(nivel):
    lista_general=["1 2","2 3","1 3"]
    lista_cambios=[]
    for i in range(3 + nivel):
        p=lista_general[random.randint(0,2)]
        lista_cambios.append(p)
    return lista_cambios


# ====================================== TKINTER ===================================== #
# ==== MOSTRAR IMAGEN ===== #
    #muestra la carta de interes
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
    root.after(7000, lambda: root.destroy())
    #muestra el meme
def mostrar_game_over():
    ancho_carta = game_over.width()
    altura_carta = game_over.height()
    canva = Canvas(width=ancho_carta + 70, height=altura_carta + 20)
    canva.pack()
    x = (ancho_carta)/2.0
    y = (altura_carta)/2.0
    canva.create_image(x + 30, y, image=game_over)
    root.after(5000, lambda: root.destroy())

# ===== MOVIMIENTO ===== #
 #time sleep es para la pocision se mantenga en cierto tiempo

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

#Primero revisar en 166linea
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
   #Segundo cero nombre de la variable, el primero es la pocision
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



# ============================================================== EJECUCION PRINCIPAL ==========================================================



print(f"\nAdivina donde está la carta ♥\n")
print(f"Hola 👋, bienvenido a nuestro juego... olvidé tu nombre, ¿podrías recordarlmelo?")
player= input("Ingrese el nombre de usuario: ")
print(f'\nHola {player}, ahora si te doy la bienvenida formal a "Adivina dónde esta la carta" \nElige una de las siguientes opciones:')

while 6>5:
    option = input("\nSeleccione: [ J ] Jugar, [ T ] Tabla de Posiciones, [ I ] Instrucciones, [ S ] Salir: ")
    if(option == "S"):
        break
    elif option =="J":
        # ============================================= Jugar ============================================= #
        nivel=1
        puntos_finales = 0
        while 5<6:
            print(f"\n========================= NIVEL {nivel} =========================")
            carticas = ['Q', 'K', 'J']
            carta_interes=mostrar_cartas(carticas) 
            print()
            if(carta_interes == 'Q'):
                print('La carta que debes seguir es la reina de corazones:')
            elif(carta_interes == 'J'):
                print("La carta que debes seguir es el jack de corazones:")
            else:
                print("La carta que debes seguir es el rey de corazones:")
            time.sleep(1)
            
    
            root = Tk() 
    
            q = PhotoImage(file="./resources/images/q.png")
            k = PhotoImage(file="./resources/images/k.png")
            j = PhotoImage(file="./resources/images/j.png") 
    
            mostrar_carta(carta_interes)
            root.mainloop() 

            print(f"¡{player} mantén los ojos abiertos mientras las cartas se mueven!")
            input("Presiona ENTER cuando estés listo(a):")

            desplazamiento = 0
            tiempo = 0
            tiempo_espera = 0
            niveles(nivel)

            root = Tk()

            q = PhotoImage(file="./resources/images/q.png")
            k = PhotoImage(file="./resources/images/k.png")
            j = PhotoImage(file="./resources/images/j.png")
            #Muestra pocisión cartas al derecho
            posicion = generar_cartas_visibles()

            root.mainloop()

            root = Tk()

            carta_escondida = PhotoImage(file="./resources/images/card.png")

            canva = ""
            longitud_carta = 0
            #Asigna las pocisiones con las cartas ya volteadas y las muestra
            posicion = generar_cartas_escondidas(posicion)

            resultado = ""

            root.after(1000, lambda: mover_cartas(posicion,cambios(nivel), desplazamiento, tiempo, carta_interes, tiempo_espera))

            root.mainloop()

            if(carta_interes == 'Q'):
                print("¿En que posición está la reina de corazones?")
            elif(carta_interes == 'J'):
                print("¿En que posición está el jack de corazones?")
            else:
                print("¿En que posición está el rey de corazones?")
            carta_seleccionada=str(input("Inserta [ I ] para la izquierda, [ M ] para el medio ó [ D ] para la derecha: "))
            if resultado==carta_seleccionada:
                nivel=nivel+1
                puntos_finales += 5
                print("\n¡Ganaste 5 puntos, pasas al siguiente nivel!")
            else:
                root = Tk()

                game_over = PhotoImage(file="./resources/images/game_over.png")

                mostrar_game_over()

                root.mainloop()
                print("\nUps! Creo que en esa posición no estaba 😥\n")
                print("\nPuntuación final:", puntos_finales)
                definir_puntaje(puntos_finales, player)

                break
    elif option == "I":
        # ============================================= Instrucciones ============================================= #
        print(f"\nLas instrucciones del juego son simples:\n\n1. Sale la carta que debes buscar.")
        print(f"2. Se te muestran tres cartas, una de ellas es la que se te indico en el paso (1), rapidamente debes memorizar sus pocisiones.\n3. Se van a voltear e intercambiarse entre ellas.\n(Como eres un principiante se comenzaran a realizar los intercambios lentamente);\n4. Finalizados los intercambios debes escoger una de las cartas;\n5. Si aciertas con la carta indicada, ganas y avanzas al siguiente nivel.\n(Los niveles aumentan de dificultad cada vez que los superas, cada nivel superado son 5 puntos)\n\n¡Mucha Suerte!")
    elif option == "T":
        # ============================================= Tabla de Posiciones ============================================= #
        tabla=archivo_leer()
        print("\n=============== Tabla de Posiciones =================\n")
        print(tabulate(tabla, headers=['Fecha', 'Usuario', 'Puntaje'], tablefmt="fancy_grid"))

    

print("\n====== Fin del Programa =========")

    

