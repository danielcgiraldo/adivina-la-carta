print(f"\nAdivina donde está La Reina de Corazones\n")
print(f"Hola, bienvenido a nuestro juego... olvidé tu nombre, ¿podrías recordarlmelo?")
player= input("Ingrese el nombre del Jugador: ")
print(f'\nHola {player}, ahora si te doy la bienvenida formal a "Adivina dónde esta La Reina de Corazones" \nElige una de las siguientes opciones: \n')
print("1. Jugar \n2. Tabla de Posiciones \n3. Instrucciones \n")
option = input("Ingresa el número de la opción que deseas elegir sin puntos ni espacios:")


# ========================== INSTRUCCIONES =========================== #
if option == "3":
    print(f"\nLas instrucciones del juego son simples:\n\n1. Salen tres cartas al azar, de estas tres cartas una de ellas es una Reina de Corazones.")
    print(f"2. Se te muestran las tres cartas, rapidamente debes memorizar sus pocisiones.\n3. Después se van a voltear e intercambiarse entre ellas.\n(Como eres un principiante se comenzaran a realizar los intercambios lentamente);\n4. Finalizados los intercambios debes escoger una de las cartas;\n5. Si aciertas con la carta de la Reina de Corazones, ganas y avanzas al siguiente nivel.\n(Los niveles aumentan de dificultad cada vez que los superas, cada nivel superado son 5 puntos)\n\n¡Mucha Suerte!")


print("\n====== Fin del Programa =========")

def g(movimientos,desplazamiento,tiempo,carta):
    cartas=["♣","♡","♠️"]
    orden=[1,2,3]
    change=random.sample(orden,k=movimientos)
    if desplazamiento<50:
        desplazamiento += 10
    if tiempo>0.01:
        tiempo -= 0.005
    pos1 = change[0]
    pos2 = change[1]
    orden[pos1], orden[pos2] = orden[pos2], orden[pos1]
    cartasrev=cartas.copy()
    cartasrev[pos1], cartasrev[pos2] = cartasrev[pos2], cartasrev[pos1]
    if cartasrev[0]=="♡":
        posi = "I"
    if cartasrev[1] =="♡":
        posi = "M"
    if cartasrev[2] == "♡":
        posi = "D"

    return (posi)
import random
def mostrar_carta(carta)
mostrar_carta=random.sample(cartas)
cartas=["♣","♡","♠️"]
orden=[0,1,2]
mensaje=["izq","medio","der"]
#Yo
cartas = ['Q', 'K', 'P']
def mostrar_cartas(lista):
    p=lista[random.randint(0,2)]
    return p
carta_a_buscar=mostrar_cartas(cartas)

# movimientos: "1 2", "2 3", "1 3"
# desplazamiento: 10, 20, 30, 40, 50
# tiempo: 0.05, 0.04, 0.03, 0.02, 0.015, 0.0145, 0.014, 0.012, 0.01
# carta: J, K, Q
# posicion: I, M, D
#tiempo_espera: 0.5, 0.4, 0.3, 0.2, 0.1, 0

# mover(movimientos, desplazamiento, tiempo, carta, tiempo_espera)
#   return posicion

nivel=1
def niveles(nivel)
if nivel<5:
    desplazamiento=10*nivel
    tiempo = 0.05
    tiempo_espera = 0.5
else:
    desplazamiento = 50
    tiempo = 0.05 - 0.005 * (nivel - 5)
    tiempo_espera = 0.5 - 0.1 * (nivel - 5)
    tiempo_espera = max(0, tiempo_espera)

