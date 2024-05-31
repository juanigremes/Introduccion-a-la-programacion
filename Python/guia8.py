#Ej 1.1
def contarLineas (nombreArchivo: str) -> int:
    archivo = open(nombreArchivo)
    leoLineas = archivo.readlines()
    return len(leoLineas)

#print(contarLineas("miArchivo.txt"))

#Ej 1.2
def pertenece (lista: list[str], palabra: str) -> bool:
    res: bool = False
    for item in lista:
        if (item == palabra):
            res = True
    return res

def armarPalabras (texto: str) -> list[str]:
    listaPalabras: list[str] = []
    palabra: str = ""
    for i in range (0,len(texto),1):
        if (texto[i] != " " and texto[i] != "\n"):
            palabra = palabra + texto[i]
        elif (palabra == "" and palabra == "\n"):
            palabra = ""
        else:
            listaPalabras.append(palabra)
            palabra = ""
    if (palabra != "" and "\n"):
        listaPalabras.append(palabra)
    return listaPalabras

#print (armarPalabras("hola que tal"))
#print (armarPalabras("   hola    que   tal "))

def existePalabra (palabra: str, nombreArchivo: str) -> bool:
    archivo = open(nombreArchivo)
    leoArchivo = archivo.read()
    archivo.close()
    res : bool = (pertenece(armarPalabras(leoArchivo),palabra))
    return res

"""
print (existePalabra("lol","miArchivo.txt"))
print (existePalabra("bien","miArchivo.txt"))
"""

#Ej 1.3
def contarApariciones (listaPalabras: list[str], palabra: str) -> int:
    contador: int = 0
    for elemento in listaPalabras:
        if elemento == palabra:
            contador += 1
    return contador

def cantidad_apariciones (nombreArchivo: str, palabra:str) -> int:
    archivo = open(nombreArchivo)
    leoArchivo = archivo.read()
    archivo.close()
    res: int = contarApariciones(armarPalabras(leoArchivo),palabra)
    return res

"""
print (cantidad_apariciones ("miArchivo.txt","hola"))
print (cantidad_apariciones ("miArchivo.txt","lol"))
print (cantidad_apariciones ("miArchivo.txt","hola"))
print (cantidad_apariciones ("miArchivo.txt","capo"))
print (cantidad_apariciones ("miArchivo.txt","teorema"))
"""

# PILAS

#Ej 8
from queue import LifoQueue as Pila
import random
def generarRandomNum (cantidad: int, desde: int, hasta: int) -> Pila[int]:
    p = Pila()
    while (cantidad != 0):
        p.put(random.randint(desde,hasta))
        cantidad -= 1
    return p

#print (generarRandomNum (5,10,20))
#print(generarRandomNum (5,10,20).queue) para poder visualizarla
