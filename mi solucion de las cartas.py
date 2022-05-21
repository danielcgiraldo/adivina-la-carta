for i in range(int(input())):
    normal = True
    color = True
    real = True
    valores = []
    palos = []
    for a in range(5):
        valores.append(int(input()))
        palos.append(input())
    valores.sort()
    for a in range(5):
        valor = valores[a]
        palo = palos[a]
        if(a == 0):
            ans_valor = valor
            ans_palo = valor
            if(valor != 10):
                real = False
        else:
            if(ans_valor + 1 != valor):
                normal = False
            if (ans_palo != palo):
                color = False
                real = False
            
        ans_palo = palo
        ans_valor = valor
    if(normal and color and not real):
        print("Escalera de color")
    elif(real):
        print("Escalera real")
    elif(normal):
        print("Escalera normal")
    elif(color):
        print("Color")
    
    else:
        print("Otra mano")
