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
def agregarFraseAlFinal (nombreArchivo: str, frase: str) -> str:
    archivo = open(nombreArchivo,'a+')
    archivo.write("\n" + frase)
    achivoConFrase = archivo.read()
    archivo.close()
    return archivoConFrase

print (agregarFraseAlFinal ("miArchivo.txt","frase agregada al final ej4"))
#ARREGLAR, NO ESTA TERMINADO  /  FIJARSE SI ESTA ARREGLADO

#Ej 5
def agregarFraseAlPrincipio (nombreArchivo: str, frase: str) -> str:
    archivo = open(nombreArchivo, 'r+')
    archivo.write(frase + "\n")
    archivoConFrase = archivo.read()
    archivo.close()
    return archivoConFrase

print (agregarFraseAlPrincipio("miArchivo.txt","frase agregada al principio ej5"))
#FIJARSE SI FUNCIONA

#Ej 6
#def listarPalabrasDeArchivo (nombreArchivo: str) -> list[str]:
# DESPUES HAGO ESTE EJERCICIO

#Ej 7 HACER ESTE TAMBIEN
#def promedioEstudiante (nombreArchivo: str, libretaUniversitaria: str) -> float:
    
#def calcularPromedioPorEstudiante (nombreArchivoNotas: str, nombreArchivoPromedios: str) -> 

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

#Ej 9
def cantidadElementos (p: Pila) -> int:
    listaAllenar = []
    while (not p.empty()):
        elementoDePila = p.get()
        listaAllenar.append(elementoDePila)
    for elemento in listaAllenar :
        p.put(elemento)
    return len(listaAllenar)

"""
print (cantidadElementos (generarRandomNum (5, 4, 60))) #deberia de dar 5
print (cantidadElementos (generarRandomNum (10, 4, 60))) # " 10
print (cantidadElementos (generarRandomNum (3, 4, 60))) # " 3
"""

#Ej 10
def buscarElMaximo (p: Pila[int]) -> int:
    listaAllenar = []
    while (not p.empty()):
        elementoDePila = p.get()
        listaAllenar.append(elementoDePila)
    maximo: int = listaAllenar[0]
    for elemento in listaAllenar:
        p.put(elemento)
        if (elemento > maximo) :
            maximo = elemento
    return maximo

"""
print (buscarElMaximo (generarRandomNum (5, 4, 60)))
print (buscarElMaximo (generarRandomNum (13, 14, 30)))
"""

#Ej 11
def contarParentesis (s: str) -> int:
    contador: int = 0
    for caracter in s:
        if caracter == '(' or caracter == ')' :
            contador += 1
    return contador

def primerParentesis (s: str) -> str:
    listaParentesis: list[str] = []
    for caracter in s:
        if caracter == '(' or caracter == ')' :
            listaParentesis.append(caracter)
    return listaParentesis[0]

def estaBienBalanceada (s: str) -> bool:
    if (contarParentesis (s) == 0):
        res = True
    elif ((contarParentesis (s))%2 != 0):
        res = False
    elif (primerParentesis(s) == '('):
        res = False
    return res

## TERMINAR ESTE TAMBIEN

#Ej 12
def pertenece (s: list[str],e: str ) -> bool:
    res: bool = False
    for elemento in s:
        if (e == elemento):
            res = True

    return res

def suma (s: list[float]) -> float:
    res: float = s[0]
    for i in range (1,len(s),1):
        res += s[i]
    return res

def resta (s: list[float]) -> float:
    res: float = s[0]
    for i in range (1,len(s),1):
        res -= s[i]
    return res

def producto (s: list[float]) -> float:
    res: float = s[0]
    for i in range (1,len(s),1):
        res = res * s[i]
    return res

def division(s: list[float]) -> float:
    res: float = s[0]
    for i in range (1,len(s),1):
        res = res / s[i]
    return res

def evaluarExpresion (s: str) -> float:
    operadores: list[str] = ['+', '-', '*' , '/']
    p = Pila()
    for elemento in s:
        if elemento != ' ' and (not pertenece(operadores,elemento)):
            p.put(float(elemento))
        elif pertenece(operadores,elemento):
            elementosAoperar: list[float] = []
            while not p.empty():
                elementosAoperar.append(p.get())
            listaVolteada: list [float] = []
            for i in range (len(elementosAoperar)-1,-1,-1):
                listaVolteada.append(elementosAoperar[i])
            if elemento == '+':
                p.put(suma(listaVolteada))
            elif elemento == '-':
                p.put(resta(listaVolteada))
            elif elemento == '*':
                p.put(producto(listaVolteada))
            elif elemento == '/':
                p.put(division(listaVolteada))
    return (p.get())

#print (evaluarExpresion("3 4 + 5 * 2 -"))

# COLAS
#Ej 13
from queue import Queue as Cola

def generarNrosAlAzar (cantidad: int, desde: int, hasta: int) -> Cola[int]:
    c = Cola()
    while cantidad != 0:
        c.put(random.randint(desde,hasta))
        cantidad -= 1
    return c

"""
print (generarNrosAlAzar (5,10,20))
print (generarNrosAlAzar (5,10,20).queue)
"""

#Ej 14
def cantidadElementosCola (c: Cola) -> int:
    listaAllenar: list[int] = []
    while not c.empty():
        listaAllenar.append(c.get())
    for elemento in listaAllenar:
        c.put(elemento)
    return len(listaAllenar)

"""
print (cantidadElementosCola (generarNrosAlAzar (7, 4, 60))) #deberia de dar 7
print (cantidadElementosCola (generarNrosAlAzar (14, 4, 60))) # " 14
print (cantidadElementosCola (generarNrosAlAzar (3, 4, 60))) # " 3
"""

#Ej 15
def buscarElMaximoCola (c: Cola) -> int:
    listaAllenar = []
    while (not c.empty()):
        elementoDeCola = c.get()
        listaAllenar.append(elementoDeCola)
    maximo: int = listaAllenar[0]
    for elemento in listaAllenar:
        c.put(elemento)
        if (elemento > maximo) :
            maximo = elemento
    return maximo

"""
print (buscarElMaximoCola (generarNrosAlAzar (5, 4, 60)))
print (buscarElMaximoCola (generarNrosAlAzar (13, 14, 30)))
"""

#Ej 16
def armarSecuenciaDeBingo() -> Cola[int]:
    de0a99: list[int] = []
    for n in range (0,100,1):
        de0a99.append(n)
    random.shuffle(de0a99)
    secuenciaRandom = Cola()
    for n in de0a99:
        secuenciaRandom.put(n)
    return secuenciaRandom

def perteneceV2 (s: list[int], e: int ) -> bool:
    res: bool = False
    for i in range (0,len(s),1):
        if (s[i] == e) :
            res = True
    return res

def jugarCartonDeBingo (carton: list[int], bolillero: Cola[int]):
    cantJugadas: int = 0
    bolilleroAux = Cola()
    conseguidos: int = 0
    while conseguidos != len(carton):
        bolita: int = bolillero.get()
        if perteneceV2 (carton,bolita):
            conseguidos += 1
        cantJugadas += 1
        bolilleroAux.put(bolita)
    while not bolillero.empty():
        bolita: int = bolillero.get()
        bolilleroAux.put(bolita)
    bolillero = bolilleroAux
    return cantJugadas

#secuencia = armarSecuenciaDeBingo()
#print(secuencia.queue)
#print (jugarCartonDeBingo ([1,4,56,78,3,2,59], secuencia))
#print (jugarCartonDeBingo ([1,4,56,78,3,2,59], armarSecuenciaDeBingo()))
#print (jugarCartonDeBingo ([1,4,56,78,3,2,59], armarSecuenciaDeBingo()))
