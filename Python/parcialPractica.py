"""
1) Acomodar [2 puntos]
El próximo 19 de Noviembre se realizará en Argentina la segunda vuelta de las
elecciones presidenciales. En esta competirán solo 2 listas (Lista UP; Lista
LLA). En la mayor parte del país los salones de las escuelas ofician de cuartos
oscuros. En ellos, las autoridades de mesa colocan las boletas sobre los
pupitres. Dado que esta elección se realizará en una eṕoca donde muy
probablemente haga mucho calor, no será raro el caso en el cual las boletas se
vuelen y mezclen a causa de ventiladores prendidos a máxima potencia. Cuando
esto ocurra, las autoridades deberán entrar al cuarto oscuro, juntar todas las
boletas, acomodarlas por partido y volver a distribuirlas en sus lugares.
Implementar una función acomodar que tome una lista con strings que
representan el nombre de lista (UP o LLA) y devuelva una lista con la misma
cantidad de elementos de cada uno de los posibles strings pero agrupadas, las
de Lista UP al principio y las de lista LLA al final.

No está permitido utilizar las funciones sort() y reverse().

problema acomodar (in s: seq<String>) : seq<String> {
    requiere: { Todos los elementos de s son o bien "LLA" o bien "UP"}
    asegura: {|res| = |s|}
    asegura: { Todos los elementos de res son o bien "LLA" o bien "UP"}
    asegura: {res contiene la misma cantidad de elementos "UP" que s}
    asegura: {res contiene todas las apariciones de "UP" antes de las
    apariciones de "LLA"}
}
Por ejemplo, dada
s = ["LLA", "UP", "LLA", "LLA", "UP"]
se debería devolver res = ["UP", "UP", "LLA", "LLA", "LLA"]
"""
def agrupar (lista: list[str]) -> list[str]:
    listaUP: list[str] = []
    listaLLA: list[str] = []
    for boleta in lista:
        if boleta == "UP":
            listaUP.append(boleta)
        else:
            listaLLA.append(boleta)
    listaOrdenada: list[str] = listaUP + listaLLA
    return listaOrdenada

#print(agrupar(["LLA", "UP", "LLA","UP","UP","LLA","LLA", "UP"]))
#print(agrupar(["LLA","UP"]))

"""
2) Posición umbral [2 puntos]
Durante una noche en un restaurant pasan varios grupos de diversa cantidad de
personas. Para llevar control de esto, el dueño va anotando en su libreta
cuánta gente entra y sale. Para hacerlo rápido decide que la mejor forma de
llevarlo adelante es escribir un número al lado del otro, usando números
positivos para los grupos que entran y negativos para los que salen. Gracias a
estas anotaciones el dueño es capaz de hacer análisis del flujo de clientes.
Por ejemplo, le interesa saber en qué momento de la noche superó una
determinada cantidad de clientes totales que ingresaron (sin importar cuántos
hay en el momento en el local).

Implementar la función pos_umbral, que dada una secuencia de enteros (puede
haber negativos) devuelve la posición en la cual se supera el valor de umbral,
teniendo en cuenta sólo los elementos positivos. Se debe devolver -1 si el
umbral no se supera en ningún momento

problema pos_umbral (in s: seq<Z>, in u: Z) : Z {
    requiere: u ≥ 0
    asegura: {res=-1 si el umbral no se supera en ningún momento }
    asegura: {Si el umbral se supera en algún momento, res es la primera
    posición tal que la sumatoria de los primeros res+1 elementos
    (considerando solo aquellos que son positivos) es estrictamente mayor que
    el umbral u }
Por ejemplo, dadas
s = [1,-2,0,5,-7,3]
u = 5
se debería devolver res = 3
"""
def pos_umbral (s: list[int], u: int) -> int:
    res: int = -1
    ingresosTotales: int = 0
    for indice in range (0, len(s), 1):
            if s[indice] > 0:
                ingresosTotales += s[indice]
            if u < ingresosTotales:
                res = indice
                return res
    return res

#print (pos_umbral([1,-2,0,5,-7,3],5))
#print (pos_umbral([1,-2,0,5,-7,3],7))
#print (pos_umbral([1,-2,0,5,-7,3],9))
#print (pos_umbral([1,-2,0,5,-7,3],0))

"""
3) Columnas repetidas [3 puntos]
Implementar la función columnas_repetidas, que dada una matriz no vacía de m
columnas (con m par y m ≥ 2) devuelve True si las primeras m/2 columnas son
iguales que las últimas m/2 columnas. Definimos a una secuencia de secuencias
como matriz si todos los elementos de la primera secuencia tienen la misma
longitud.


problema columnas_repetidas(in mat:seq<seq<Z>> ) : Bool {
    requiere: {|mat| > 0}
    requiere: {todos los elementos de mat tienen igual longitud m, con m > 0
    (los elementos de mat son secuencias)}
    requiere: {todos los elementos de mat tienen longitud par (la cantidad de
    columnas de la matriz es par)}
    asegura: {(res = true) <=> las primeras m/2 columnas de mat son iguales a
    las últimas m/2 columnas}
}

Por ejemplo, dada la matriz
m = [[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]
se debería devolver res = true
TIP: para dividir un número entero x por 2 y obtener como resultado un número
entero puede utilizarse la siguiente instrucción: int(x/2)
"""
def columnas_repetidas (matriz: list[list[int]]) -> bool:
    res: bool = True
    for fila in matriz:
        primeraMitad: list[int] = []
        segundaMitad: list[int] = []
        indice: int = 0
        while indice < len(fila)/2:
            primeraMitad.append(fila[indice])
            indice += 1
        for i in range (indice, len(fila), 1):
            segundaMitad.append(fila[i])
        if primeraMitad != segundaMitad:
            res = False
    return res

#print(columnas_repetidas([[1,2,1,2],[-5,6,-5,6],[0,1,0,1]]))
#print(columnas_repetidas([[1,2,1,2],[6,6,-5,6],[0,1,0,1]]))
#print(columnas_repetidas([[1,2,1,2],[-5,6,-5,6]]))
#print(columnas_repetidas([[1,2,1,2],[-5,6,-5,9]]))
       
"""
4) Rugby 4 naciones [3 puntos]
Desde hace más de 10 años existe en el mundo del rugby un torneo que disputan
anualmente 4 selecciones del sur global (Argentina, Australia, Nueva Zelanda y
Sudáfrica). Este torneo se llama "The rugby championship" o comunmente "4
naciones", ya que suplantó al viejo "3 naciones".

Implementar la función cuenta_posiciones_por_nacion que dada la lista de
naciones que compiten en el torneo, y el diccionario que tiene los resultados
de los torneos anuales en el formato año:posiciones_naciones, donde año es un
número entero y posiciones_naciones es una lista de strings con los nombres de
las naciones, genere un diccionario de naciones:#posiciones, que para cada
Nación devuelva la lista de cuántas veces salió en esa posición.

Tip: para crear una lista con tantos ceros como naciones se puede utilizar la
siguiente sintaxis lista_ceros = [0]*len(naciones)

problema cuenta_posiciones_por_nacion(in naciones: seq<String>, in torneos:
dict<Z,seq<String>>: dict<String,seq<Z>> {
    requiere: {naciones no tiene elementos repetidos}
    requiere: {Los valores del diccionario torneos son permutaciones de la
    lista naciones (es decir, tienen exactamente los mismos elementos que
    naciones, en cualquier orden posible)}
    asegura: {res tiene como claves los elementos de naciones}
    asegura: {El valor en res de una nación es una lista de |naciones|
    elementos que indica en la posición i cuántas veces salió esa nación en la
    i-ésima posición.}
}
Por ejemplo, dados
naciones= ["arg", "aus", "nz", "sud"]
torneos= {2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}
se debería devolver res = {"arg": [0,0,1,1], "aus": [0,0,1,1], "nz": [2,0,0,0],
"sud": [0,2,0,0]}
"""
def cuenta_posiciones_por_nacion (naciones: list[str], torneos: dict[int,list[str]]) -> dict[str,list[int]]:
    res: dict[str,list[int]] = {}
    for pais in naciones:
        res[pais] = [0]*len(naciones)
    for ano in torneos:
        listaPosiciones: list[str] = torneos[ano]
        for i in range(0,len(listaPosiciones),1):
            buscoPais = res[listaPosiciones[i]]
            buscoPais[i] += 1
            res[listaPosiciones[i]] = buscoPais
    return res

#print(cuenta_posiciones_por_nacion(["arg", "aus", "nz", "sud"],{2023:["nz", "sud", "arg", "aus"], 2022:["nz", "sud", "aus", "arg"]}))