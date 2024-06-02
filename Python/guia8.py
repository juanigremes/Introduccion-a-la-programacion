#Ej 1.1
def contarLineas (nombreArchivo: str) -> int:
    archivo = open(nombreArchivo,'r')
    leoLineas = archivo.readlines()
    archivo.close()
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
    archivo = open(nombreArchivo,'r')
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
    archivo = open(nombreArchivo,'r')
    leoArchivo = archivo.read()
    archivo.close()
    res: int = contarApariciones(armarPalabras(leoArchivo),palabra)
    return res

"""
print (cantidad_apariciones ("miArchivo.txt","hola"))
print (cantidad_apariciones ("miArchivo.txt","lol"))
print (cantidad_apariciones ("miArchivo.txt","siu"))
print (cantidad_apariciones ("miArchivo.txt","capo"))
print (cantidad_apariciones ("miArchivo.txt","teorema"))
"""

#Ej 2
def identificarPrimerCaracter(linea: list[str]) -> str:
    primerCaracter: str = ""
    indice: int = 0
    while linea[indice] == ' ':
        indice += 1
    if linea[indice] == '#':
        primerCaracter = '#'
    else:
        primerCaracter = str(linea[indice])
    return primerCaracter

def caracterValido (caracter: str) -> bool:
    res: bool = True
    if caracter == '#':
        res = False
    return res

def clonar_sin_comentarios (nombreArchivo: str) -> str:
    archivoOriginal = open(nombreArchivo,'r')
    lineasArchivo = archivoOriginal.readlines()
    archivoOriginal.close()
    archivoSinComentarios: str = []
    for linea in lineasArchivo :
        if caracterValido(identificarPrimerCaracter(linea)):
            archivoSinComentarios.append(linea)
    archivoFinal: str = ""
    for n in range (0,len(archivoSinComentarios),1):
        archivoFinal = archivoFinal + archivoSinComentarios[n]
    return archivoFinal

#print (clonar_sin_comentarios("miArchivo.txt"))

#Ej 3
def invertirLineas (nombreArchivo: str) -> str:
    archivoOriginal = open(nombreArchivo,'r')
    lineasArchivo = archivoOriginal.readlines()
    archivoOriginal.close()
    archivoCasiInvertido: str = []
    for linea in lineasArchivo:
        lineaInvertida: str = ""
        for n in range (0,len(linea),1):
            lineaInvertida = linea[n] + lineaInvertida
        archivoCasiInvertido.append(lineaInvertida)
    archivoInvertido: str = ""
    for linea in archivoCasiInvertido:
        for n in range (0,len(archivoCasiInvertido),1):
            archivoInvertido = archivoCasiInvertido[n] + archivoInvertido
    return archivoInvertido
    
#print (invertirLineas("miArchivo.txt"))
# SOLAMENTE TENIA QUE INVERTIR LAS LINEAS E INVERTI todo el TEXTO

#Ej 4
def agregarFraseAlFinal (nombreArchivo: str, frase: str):
    archivo = open(nombreArchivo,'a+')
    archivo.write("\n" + frase)
    achivoConFrase = archivo.read()
    archivo.close
    return archivoConFraseLeido

print (agregarFraseAlFinal ("miArchivo.txt","frase agregada al final"))
#ARREGLAR, NO ESTA TERMINADO  /  FIJARSE SI ESTA ARREGLADO

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
