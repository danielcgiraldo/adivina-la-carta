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
    orden=[1,2,3]
    change=random.sample(orden,k=movimientos)
    if desplazamiento != 50:
        desplazamiento += 10
    if tiempo>0.01:
        tiempo -= 0.005
    tiempo=[0.05,0.04,0.03,0.02,0.01]
    pos1 = change[0]
    pos2 = change[1]
    orden[pos1], orden[pos2] = orden[pos2], orden[pos1]
    
    
    
    if rta == "I":
        posi = 0
    elif rta == "M":
        posi = 1
    elif rta == "D":
        posi = 2

    return (posi)
import random
cartas=["♣","♡","♠️"]
orden=[0,1,2]
mensaje=["izq","medio","der"]
change=random.sample(orden,k=2)
print(change)
print(cartas)

cartasrev=cartas.copy()
cartasrev[pos1], cartasrev[pos2] = cartasrev[pos2], cartasrev[pos1]
print(cartasrev)
print(f"Intercambio {mensaje[pos1]} con {mensaje[pos2]}")
def f(n):
    cartas=["♣","♡","♠️"]
    orden=[0,1,2]
    mensaje=["izq","medio","der"]
    change=random.sample(orden,k=2)
    print(change)
    print(cartas)
    pos1 = change[0]
    pos2 = change[1]
    orden[pos1], orden[pos2] = orden[pos2], orden[pos1]
    cartasrev=cartas.copy()
    cartasrev[pos1], cartasrev[pos2] = cartasrev[pos2], cartasrev[pos1]
    print(cartasrev)
    print(f"Intercambio {mensaje[pos1]} con {mensaje[pos2]}")
    for i in range(n):
        change=random.sample(orden,k=2)
        pos1 = change[0]
        pos2 = change[1]
        cartasrev[pos1], cartasrev[pos2] = cartasrev[pos2], cartasrev[pos1]
        print(cartasrev)
        print(f"Intercambio {mensaje[pos1]} con {mensaje[pos2]}")
    return cartasrev

print("Pon las letras 'I' para la pocision izquierda, 'M' para la del medio y 'D' para la derecha, sin comas y en mayusculas")
rta=str(input("¿Dónde esta la reina de corazones?: "))
n=1
if rta == "I":
    posi = 0
elif rta == "M":
    posi = 1
elif rta == "D":
    posi = 2
if cartasrev[posi]:
    print("has ganado 5 ptos, pasas al siguiente nivel")
    f(n)
    n=n+1
    print("Pon las letras 'I' para la pocision izquierda, 'M' para la del medio y 'D' para la derecha, sin comas y en mayusculas")
    rta=str(input("¿Dónde esta la reina de corazones?: "))
    if rta == "I":
        posi = 0
    elif rta == "M":
        posi = 1
    elif rta == "D":
        posi = 2
else:
    print("game over")