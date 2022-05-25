print(f"\nAdivina donde está La Reina de Corazones\n")
print(f"Hola, bienvenido a nuestro juego... olvidé tu nombre, ¿podrías recordarlmelo?")
player= input("Ingrese el nombre del Jugador: ")
player=player.capitalize()
print(f'\nHola {player}, ahora si te doy la bienvenida formal a "Adivina dónde esta La Reina de Corazones" \nElige una de las siguientes opciones: \n')
print("1. Jugar \n2. Tabla de Posiciones \n3. Instrucciones \n")
option = input("Ingresa el número de la opción que deseas elegir sin puntos ni espacios:")


# ========================== INSTRUCCIONES =========================== #
if option =="1":
    #Función Canva Daniel
    m
elif option == "3":
    print(f"\nLas instrucciones del juego son simples:\n\n1. Salen tres cartas al azar, de estas tres cartas una de ellas es una Reina de Corazones.")
    print(f"2. Se te muestran las tres cartas, rapidamente debes memorizar sus pocisiones.\n3. Después se van a voltear e intercambiarse entre ellas.\n(Como eres un principiante se comenzaran a realizar los intercambios lentamente);\n4. Finalizados los intercambios debes escoger una de las cartas;\n5. Si aciertas con la carta de la Reina de Corazones, ganas y avanzas al siguiente nivel.\n(Los niveles aumentan de dificultad cada vez que los superas, cada nivel superado son 5 puntos)\n\n¡Mucha Suerte!")
elif option == "2":
    print(f"No disponible :/, estamos trabajando en ello")

print("\n====== Fin del Programa =========")
nivel=1
import random
carticas = ['Q', 'K', 'P']
def mostrar_cartas(lista):
    p=lista[random.randint(0,2)]
    return p
carta_interes=mostrar_cartas(carticas)
def niveles(nivel):
    if nivel<5:
        desplazamiento=10*nivel
        tiempo = 0.05
        tiempo_espera = 0.5
    else:
        desplazamiento = 50
        tiempo = 0.05 - 0.005 * (nivel - 5)
        tiempo_espera = 0.5 - 0.1 * (nivel - 5)
        tiempo_espera = max(0, tiempo_espera)
def cambios(nivel):
    lista_general=["1 2","2 3","1 3"]
    lista_cambios=[]
    for i in range(nivel+4):
        p=lista_general[random.randint(0,2)]
        lista_cambios.append(p)
    return lista_cambios
while 5<6:
    carta_seleccionada=str(input("Inserta [D] para la derecha, [M] para el medio ó [I] para la izquierda"))
    if resultado==carta_seleccionada:
        nivel=nivel+1
        niveles(nivel)
        cambios(nivel)
        print("Ganste 5 puntos, pasas al siguiente nivel")
    else:
        print("game over")
        break



    

