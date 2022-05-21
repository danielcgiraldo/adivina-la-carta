def palosconsec(lista):
    d=lista.count("D")
    t=lista.count("T")
    p=lista.count("P")
    c=lista.count("C")
    if c==5 or d==5 or p==5 or t==5:
        return True
    else:
        return False
def numeroconsec(lista):
    lisr=[]
    las=[-4,-2,0,2,4]
    supremos=[10,11,12,13,14]
    lista.sort()
    lit=lista.copy()
    lit.reverse()
    for i in range(0,len(lit)):
        p=lista[i]-lit[i]
        lisr.append(p)
    q=0
    n=0
    m=0
    res=0
    for j in lisr:
        if j==las[q]:
            n=n+1
        q=q+1
    for j in supremos:
        if j==lista[res]:
            m=m+1
        res=res+1
    if m==5:
        return ("Real")
    elif n==5 and lista[2] != lista[3]: #Aqui esta el cambiecito
        return True
    else:
        return False
l=[]
m=[]
respuesta=[]
k=int(input())
for j in range(k):
    for i in range(5):
        number=int(input())
        l.append(number)
        palo=str(input())
        m.append(palo)
    P=palosconsec(m)
    N=numeroconsec(l)
    if N=="Real" and P==True:
        rta="Escalera real"
    elif P==True and N==True:
        rta="Escalera de color"
    elif P==True:
        rta="Color"
    elif N==True:
        rta="Escalera normal"
    else:
        rta="Otra mano"
    respuesta.append(rta)
    l.clear()
    m.clear()
for i in respuesta:
    print(i)
