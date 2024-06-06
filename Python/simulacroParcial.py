# no tuve este simulacro, es de un año anterior
"""
 Ejercicio 1

  problema ultima_aparicion (s: seq⟨Z⟩, e: Z) : Z {
    requiere: {e pertenece a s }
    asegura: {res es la posición de la última aparición de e en s}
  }
"""
def ultimaAparicion (s: list[int], e: int) -> int:
    res: int = 0
    for i in range (0, len(s), 1):
        if s[i] == e:
            res = i
    return res

#print(ultimaAparicion([-1,4,0,4,100,0,100,0,-1,-1],0))
#print(ultimaAparicion([-1,4,0,4,100,0,100,0,-1,-1],-1))
#print(ultimaAparicion([-1,4,0,4,100,0,100,0,-1,-1],100))

"""
 Ejercicio 2

  problema elementos_exclusivos (s: seq⟨Z⟩, t: seq⟨Z⟩) : seq⟨Z⟩ {
    requiere: -
    asegura: {Los elementos de res pertenecen o bien a s o bien a t, pero no a ambas }
    asegura: {res no tiene elementos repetidos }
  }
"""
def pertenece (elemento, lista: list) -> bool:  #LE SAQUE LOS TIPOS DE INT PORQUE LA REUTILICE EN OTRO EJERCICIO CON STR
    res: bool = False
    for n in lista:
        if n == elemento:
            res = True
    return res

def elementosExclusivos (s: list[int], t: list[int]) -> list[int]:
    listaFinal: list[int] = [] 
    for elemento in s:
        if not pertenece(elemento,t) and not pertenece(elemento,listaFinal):
            listaFinal.append(elemento)
    for elemento in t:
        if not pertenece(elemento,s) and not pertenece(elemento,listaFinal):
            listaFinal.append(elemento)
    res: list[int] = listaFinal #devolveria directamente la listaFinal pero no se si tengo que repetar los nombres de la especificacion
    return res

#print(elementosExclusivos([-1,4,0,4,3,0,100,0,-1,-1],[0,100,5,0,100,-1,5]))
#print(elementosExclusivos([],[0,100,5,0,100,-1,5]))
#print(elementosExclusivos([0,100,5,0,100,-1,5],[]))
#print(elementosExclusivos([],[]))

"""
 Ejercicio 3

 Se cuenta con un diccionario que contiene traducciones de palabras del idioma castellano (claves) a palabras
 en inglés (valores), y otro diccionario que contiene traducciones de palabras en castellano (claves) a palabras
 en alemán (valores). Se pide escribir un programa que dados estos dos diccionarios devuelva la cantidad de 
 palabras que tienen la misma traducción en inglés y en alemán.

  problema contar_traducciones_iguales (ing: dicc⟨String,String⟩, ale: dicc⟨String,String⟩) : Z {
    requiere: -
    asegura: {res = cantidad de palabras que están en ambos diccionarios y además tienen igual valor en ambos}
  }
"""
def contarTraduccionesIguales (idioma1: dict[str,str], idioma2: dict[str,str]) -> int:
    contador: int = 0
    for palabra in idioma1.keys():
        if pertenece(palabra,idioma2.keys()) and idioma1[palabra] == idioma2[palabra]:
            contador += 1
    return contador

#aleman = {"Mano": "Hand", "Pie": "Fuss", "Dedo": "Finger", "Cara": "Gesicht"}
#ingles = {"Pie": "Foot", "Dedo": "Finger", "Mano": "Hand"}
#print(contarTraduccionesIguales(ingles,aleman))

"""
 Ejercicio 4

 Dada una lista de enteros s, se desea devolver un diccionario cuyas claves sean los valores presentes en s, 
 y sus valores la cantidad de veces que cada uno de esos números aparece en s

  problema convertir_a_diccionario (lista: seq⟨Z⟩) : dicc⟨Z,Z⟩) {
    requiere: -
    asegura: {res tiene como claves los elementos de lista y res[n] = cantidad de veces que aparece n en lista}
  }
"""
def convertirAdiccionario(lista: list[int]) -> dict[int,int]:
    diccionario: dict[int,int] = {}
    for elemento in lista:
        if pertenece(elemento,diccionario.keys()):
            diccionario[elemento] += 1
        else:
            diccionario[elemento] = 1
    return diccionario

#print(convertirAdiccionario([-1,0,4,100,100,-1,-1]))