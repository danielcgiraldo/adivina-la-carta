print(f"\nAdivina donde está La Reina de Corazones\n")
print(f"Hola, bienvenido a nuestro juego... olvidé tu nombre, ¿podrías recordarlmelo?")
player= input("Ingrese el nombre del Jugador: ")
print(f'\nHola {player}, ahora si te doy la bienvenida formal a "Adivina dónde esta La Reina de Corazones" \nElige una de las siguientes opciones: \n')
print("1. Jugar \n2. Tabla de Posiciones \n3. Instrucciones \n")
option = input("Ingresa el número de la opción que deseas elegir sin puntos ni espacios:")


# ========================== INSTRUCCIONES =========================== #
if option == "3":
    print(f"\nLas instrucciones del juego son simples:\n\n1. Salen tres cartas al azar, de estas tres cartas una de ellas es una Reina de Corazones.")
    print(f"2. Se te muestran las tres cartas, rapidamente debes memorizar sus pocisiones.\n3. Después se van a voltear e intercambiarse entre ellas.\n(Como eres un principiante se comenzaran a realizar los intercambios lentamente);\n4. Finalizados los intercambios debes escoger una de las cartas;\n5. Si aciertas con la carta de la Reina de Corazones, ganas y avanzas al siguiente nivel.\n(Los niveles aumentan de dificultad cada vez que los superas)\n\n¡Mucha Suerte!")


print("\n====== Fin del Programa =========")