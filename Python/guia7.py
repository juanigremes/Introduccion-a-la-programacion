#PRIMERA PARTE

#Ej 1.1
def pertenece (s: list[int],e: int ) -> bool:
    res: bool = False
    for elemento in s:
        if (e == elemento):
            res = True

    return res

def perteneceV2 (s: list[int], e: int ) -> bool:
    res: bool = False
    for i in range (0,len(s),1):
        if (s[i] == e) :
            res = True
    
    return res

def perteneceV3 (s: list[int], e: int ) -> bool:
    res: bool = False
    i = 0
    while (i < (len(s)) and res == False):
        if (s[i] == e):
            res = True
        else:
            i += 1
    
    return res
#puedo sacar el else y ("res == false") y que i+=1 pase siempre, va a frenar cuando  i sea mayor al indice

("""
print (perteneceV3 ([1,2,3,4,5],5))
print (perteneceV3 ([1,2,3,4,5],6))
print (perteneceV3 ([1,2,3,4,5],1))
print (perteneceV3 ([1,2,3,4,5],7))
""")

#Ej 1.2
def divide_a_todos (s: list[int], e:int) -> bool:
    res: bool = True
    for elemento in s:
        if ((elemento%e) != 0):
            res = False

    return res

("""
print (divide_a_todos ([2,4,6,8,10],2))
print (divide_a_todos ([2,4,6,8,11],2))
print (divide_a_todos ([5,10,15,20],5))
print (divide_a_todos ([5,11,15,20],5))
""")

#Ej 1.3
def suma_total (s: list[int]):
    total: int = 0
    for elemento in s:
        total += elemento

    return total

("""
print (suma_total ([1,1,1,2]))
print (suma_total ([1,2,3,4,5]))
""")

#Ej 1.4
def ordenados (s:list[int]) -> bool:
    res: bool = True
    if (len(s) == 0):
        return res
    else:
        i:int = 0
        j:int = 1
        while ((j < len(s)) and (res == True)):
            primerElemento:int = s[i]
            segundoElemento: int = s[j]
            if (primerElemento > segundoElemento):
                res = False
            else:
                i += 1
                j += 1

    return res

("""
print (ordenados ([1,2,3,4,5]))
print (ordenados ([1,2,3,5,4]))
print (ordenados ([1,3,2,4,5]))
""")

#Ej 1.5
def palabraLarga (palabras: list[str]) -> bool:
    res: bool = False
    for palabra in palabras:
        if (len(palabra) > 7):
            res = True

    return res

("""
print (palabraLarga (["hola","letra","primo"]))
print (palabraLarga (["hola","letra","barbaridad"]))
""")

#Ej 1.6
def palindrome (palabra: str) -> bool:
    res = False
    palabraReves: str = ""
    for letra in palabra:
        palabraReves = letra + palabraReves

    if (palabraReves == palabra) :
        res = True

    return res

"""
print (palindrome ("kayak"))
print (palindrome ("carlos")) 
print (palindrome ("anana"))
"""

#Ej 1.7
def fortaleza (contraseña: str) -> str:
    minusculas: int = 0
    mayusculas: int = 0
    numeros: int = 0

    for caracter in contraseña:
        if ( 'a' <= caracter <= 'z' ):
            minusculas += 1
        elif ( 'A' <= caracter <= 'Z' ):
            mayusculas +=1
        elif ( '0' <= caracter <= '9' ):
            numeros += 1
    
    if (len(contraseña) > 8) and (minusculas >= 1) and (mayusculas >= 1) and (numeros >= 1):
        return ("VERDE")
    elif (len(contraseña) < 5):
        return ("ROJA")
    else:
        return ("AMARILLA")

"""
print (fortaleza ("Contraseña2024"))
print (fortaleza ("pablo43"))
print (fortaleza ("pila"))
"""

#Ej 1.8
def saldoActual (operaciones: list[tuple[str,int]]) -> int:
    saldoFinal: int = 0
    for tupla in operaciones:
        if (tupla[0] == "I"):
            saldoFinal += tupla[1]
        elif (tupla[0] == "R"):
            saldoFinal -= tupla[1]

    return saldoFinal

#print (saldoActual([("I",2000), ("R", 20),("R", 1000),("I", 300)]))

#Ej 1.9

def perteneceV9 (s: list[str],e: str ) -> bool:
    res: bool = False
    for elemento in s:
        if (e == elemento):
            res = True

    return res

def sacarRepetidosV9 (inicial: list[str]) -> list[str]:
    final: list[str] = ""
    for v in inicial:
        if (not (perteneceV9 (final,v))):
            final = v + final

    return final

def tresVocalesDistintas (palabra: str) -> bool:
    res: bool = False
    vocales: list[str] = ["a","e","i","o","u","A","E","I","O","U"]
    soloVocales: str = ""
    for letra in palabra:
        if (perteneceV9(vocales,letra)):
            soloVocales = letra + soloVocales
    
    if (len (sacarRepetidosV9(soloVocales)) >= 3):
        res = True

    return res

"""
print (tresVocalesDistintas("murcielago"))
print (tresVocalesDistintas("camion"))
print (tresVocalesDistintas("Abracemos"))
print (tresVocalesDistintas("loro"))
"""

#SEGUNDA PARTE

#Ej 2.1
def sacoPares (lista: list[int]) -> list[int]:
    for indice in range (0,len(lista),1):
        if (indice % 2 == 0):
            lista[indice] = 0
            
    return lista

#print (sacoPares ([1,2,3,4,5,6,7,8,9]))

#Ej 2.2
def sacoParesV2 (lista: list[int]) -> list[int]:
    listamodificada: list[int] = lista
    for indice in range (0,len(lista),1):
        if (indice % 2 == 0):
            listamodificada[indice] = 0
            
    return listamodificada

#print (sacoParesV2 ([1,2,3,4,5,6,7,8,9]))

#Ej 2.3
def sacoVocales (palabra: list[str]) -> list[str]:
    vocales: list[str] = ["a","e","i","o","u","A","E","I","O","U"]
    sinVocales: list[str] =""
    for letra in palabra:
        if (not perteneceV9 (vocales,letra)):
            sinVocales = sinVocales + letra

    return sinVocales

#print (sacoVocales ("palabra"))

#Ej 2.4
def reemplaza_vocales (palabra: list[str]) -> list[str]:
    vocales: list[str] = ["a","e","i","o","u"]
    sinVocales: list[str] =""
    for letra in palabra:
        if (not perteneceV9 (vocales,letra)):
            sinVocales = sinVocales + letra
        else:
            sinVocales = sinVocales + "_"

    return sinVocales

#print (reemplaza_vocales("palabra"))

#Ej 2.5
def da_vuelta_str (secuencia: list[str]) -> list [str]:
    aicneuces: str = ""
    for letra in secuencia:
        aicneuces = letra + aicneuces

    return aicneuces

#print (da_vuelta_str("lolardo"))

#Ej 2.6
def sacarRepetidosV26 (secuencia: list[str]) -> list[str]:
    final: list[str] = ""
    for v in secuencia:
        if (not (perteneceV9 (final,v))):
            final = v + final

    return final

#Ej 3
def aprobado (notas: list[int]) -> int:
    buenaNota: int = 0
    insuficiente: int = 0

    for nota in notas:
        if (nota >= 4):
            buenaNota += 1
        else:
            insuficiente += 1
    
    if (insuficiente >= 1):
        res = 3
    else:
        if (promedio (notas) >= 7):
            res = 1
        else:
            res = 2
    
    return res

def promedio (lista: list[int]) -> float:
    sumatotal: float = 0
    
    for n in lista:
        sumatotal += n
    
    final = sumatotal / (len(lista)) 
        
    return final

"""
print (aprobado([5,5,5,5,5]))
print (aprobado([8,8,8,8,8]))
print (aprobado([4,3,4,4,4]))
"""

#Ej 4.1
def misEstudiantes () -> list[str]:
    estudiantes: list[str] = []
    while (True):
        estudiante = input("introducir nombre estudiante o listo:")
        if (estudiante == "listo") :
            return estudiantes
        else:
            estudiantes.append(estudiante)

#print(misEstudiantes())

#Ej 4.2
def historialSUBE () -> list[tuple[str,float]]:
    historial: list[tuple[str,float]] = []
    tupla: tuple[str,float] = []
    while (True):
        operacion = input("introducir C , D o X: ")
        if (operacion == "C"):
            monto = input("monto a cargar: ")
            tupla = ["C",monto]
            historial.append(tupla)
        elif (operacion == "D"):
            monto = input("monto a descontar: ")
            tupla = ["D",monto]
            historial.append(tupla)
        elif (operacion == "X"):
            return historial

#print (historialSUBE())

#Ej 4.3
import random
def sieteYMedio () -> list[float]:

    cartaInicial: float = random.choice([1,2,3,4,5,6,7,10,11,12])
    print ("sacó la carta " + str(cartaInicial))
    if (cartaInicial == 10 or cartaInicial == 11 or cartaInicial == 12):
        cartaInicial = 0.5
        print ("tenés: 0.5 puntos")
    else:
        print ("tenés: " + str(cartaInicial) + " puntos")

    sumaCartas: float = cartaInicial
    historialCartas: list[float] = [cartaInicial]

    while (sumaCartas <= 7.5):
        siguienteReparto = input("querés sacar otra carta [si] o plantarte [no]? ")

        if (siguienteReparto == "si"):
            repartirCarta: float = random.choice([1,2,3,4,5,6,7,10,11,12])
            print ("sacó la carta " + str(repartirCarta))
            if (repartirCarta == 10 or repartirCarta == 11 or repartirCarta == 12):
                repartirCarta = 0.5
            sumaCartas += repartirCarta
            print ("tenés: " + str(sumaCartas) + " puntos")
            historialCartas.append(repartirCarta)

        elif (siguienteReparto == "no"):
            print ("te plantas")
            print ("tenés: " + str(sumaCartas) + " puntos")
            print ("estas fueron tus cartas:")
            return historialCartas
        
    print ("perdiste")
    print ("estas fueron tus cartas:")
    return historialCartas

#print (sieteYMedio())

#Ej 5.1
def pertenece_a_cada_uno_version_1 (s: list[list[int]], e: int, res: list[bool]) -> list[bool]:
    for i in range (0,len(s),1):
        if (i >= len(res)):
            res.append(pertenece (s[i],e))
        else:
            res[i] = pertenece (s[i],e)
    for resto in range (i+1,len(res),1):
        res[resto] = False
    return res

#print(pertenece_a_cada_uno_version_1([[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]],4,[True,False]))
#print(pertenece_a_cada_uno_version_1([[2,3,4]],4,[True,True,True,True,True]))

#Ej 5.2
def pertenece_a_cada_uno_version_2 (s: list[list[int]], e: int, res: list[bool]) -> list[bool]:
    res = []
    #PUEDO USAR UN "res.clear()" en vez de "res = []"
    for lista in s:
        res.append(pertenece(lista,e))
    return res

#print(pertenece_a_cada_uno_version_2([[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]],4,[True,False]))
#print(pertenece_a_cada_uno_version_2([[2,3,4]],4,[True,True,True,True,True]))

#Ej 5.3
def es_matriz (posibleMatriz: list[list[int]]) -> bool:
    res: bool = False
    if (len(posibleMatriz) == 0):
        return res
    elif (len(posibleMatriz[0]) == 0):
        return res
    else:
        for i in range (1,len(posibleMatriz),1):
            if len(posibleMatriz[i-1]) != len(posibleMatriz[i]):
                return res
        res = True
        return res
    
"""
print (es_matriz ([[1,2,3],[1,2,3],[1,2,3]]))
print (es_matriz ([[1,2,3],[1,2,3],[1,2]]))
print (es_matriz ([[1,2,3],[1,3],[1,2,3]]))
print (es_matriz ([[1],[1,3],[1,2,3]]))
print (es_matriz ([[1],[1,3,5],[1,2,3]]))
"""

#Ej 5.4
def filas_ordenadas (matriz: list[list[int]], res: list[bool]) -> list[bool]:
    for i in range (0,len(matriz),1):
        if (i >= len(res)):
            res.append(ordenados(matriz[i]))
        else:
            res[i] = ordenados(matriz[i])
    for resto in range (i+1,len(res),1):
        res[resto] = False
    return res

"""
print (filas_ordenadas([[1,2,3],[2,3,4],[4,5,6]],[True]))
print (filas_ordenadas([[1,2,3],[2,3,4],[4,5,6]],[True,False,False,False]))
print (filas_ordenadas([[1,2,3],[2,3,4],[4,7,6]],[True]))
print (filas_ordenadas([[1,2,3],[2,8,4],[4,5,6]],[True,False,False,False]))
"""

#Ej 5.5
