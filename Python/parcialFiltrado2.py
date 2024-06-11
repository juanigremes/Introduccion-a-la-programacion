#Ej 1 - FILA EN EXACTABANK
from queue import Queue as Cola

def reordenar_cola_priorizando_vips (filaClientes: Cola[tuple[str,str]]) -> Cola[str]:
    colaAuxiliar: Cola[tuple[str,str]] = Cola()
    colaVIP: Cola[str] = Cola()
    colaComun: Cola[str] = Cola()
    while not filaClientes.empty():
        cliente: tuple[str,str] = filaClientes.get()
        if cliente[1] == 'comun':
            colaComun.put(cliente[0])
        elif cliente[1] == 'vip':
            colaVIP.put(cliente[0])
        colaAuxiliar.put(cliente)
    res: Cola[str] = Cola()
    while not colaVIP.empty():
        cliente: str = colaVIP.get()
        res.put(cliente)
    while not colaComun.empty():
        cliente: str = colaComun.get()
        res.put(cliente)
    while not colaAuxiliar.empty():
        cliente: str = colaAuxiliar.get()
        filaClientes.put(cliente)
    return res

#Ej 2 - CHICKEN GAME
def resultados (estrategia1: str, estrategia2: str, puntosActuales: tuple[int,int]) -> list[int,int]:
    res: list[int,int] = list(puntosActuales)
    if estrategia1 == "me la banco y no me desvio" and estrategia2 == "me la banco y no me desvio":
        res[0] -= 5
        res[1] -= 5
    elif estrategia1 == "me la banco y no me desvio" and estrategia2 == "me desvio siempre":
        res[0] += 10
        res[1] -= 15
    elif estrategia1 == "me desvio siempre" and estrategia2 == "me la banco y no me desvio":
        res[0] -= 15
        res[1] += 10
    elif estrategia1 == "me desvio siempre" and estrategia2 == "me desvio siempre":
        res[0] -= 10
        res[1] -= 10
    return res

def torneo_de_gallinas (estrategias: dict[str,str]) -> dict[str,int]:
    res: dict[str,int] = {}
    for jugador in estrategias.keys():
        res[jugador] = 0
    
    jugadores = list(estrategias.keys())
    estrategiasJugadores = list(estrategias.values())
    listaPartidas: list[tuple[str,str]] = []
    listaPartidasJugadores: list[tuple[str,str]] = []

    for i in range (0, len(jugadores), 1):
        for n in range (i+1, len(jugadores), 1):
            listaPartidas.append([estrategiasJugadores[i],estrategiasJugadores[n]])
            listaPartidasJugadores.append([jugadores[i],jugadores[n]])

    for i in range (0, len(listaPartidas), 1):
        jugador1 = listaPartidasJugadores[i][0]
        jugador2 = listaPartidasJugadores[i][1]
        estrategia1 = listaPartidas[i][0]
        estrategia2 = listaPartidas[i][1]
        resultadoPartida = resultados(estrategia1, estrategia2, tuple([res[jugador1],res[jugador2]]))
        res[jugador1] = resultadoPartida[0]
        res[jugador2] = resultadoPartida[1]
        
    return res

"""def hagodiccionario (lista: list[tuple[str,str]]) -> dict[str,str]:
    res: dict[str,str] = {}
    for tupla in lista:
        res[tupla[0]] = tupla[1]
    return res"""

#print(torneo_de_gallinas(hagodiccionario([["m","me desvio siempre"],["j","me desvio siempre"],["p","me la banco y no me desvio"],["l","me desvio siempre"],["o","me la banco y no me desvio"]])))

#Ej 3 - TA TE TI FACILITO
def ganoX (columna: list[str]) -> bool:
    res = False
    contadorConsecutivosMax = 0
    contadorConsecutivos: int = 0
    for letra in columna:
        if letra == 'X':
            contadorConsecutivos += 1
        else:
            if contadorConsecutivosMax < contadorConsecutivos:
                contadorConsecutivosMax = contadorConsecutivos
            contadorConsecutivos = 0
        if contadorConsecutivosMax < contadorConsecutivos:
            contadorConsecutivosMax = contadorConsecutivos
    if contadorConsecutivosMax >= 3:
        res = True
    return res

def ganoO (columna: list[str]) -> bool:
    res = False
    contadorConsecutivosMax = 0
    contadorConsecutivos: int = 0
    for letra in columna:
        if letra == 'O':
            contadorConsecutivos += 1
        else:
            if contadorConsecutivosMax < contadorConsecutivos:
                contadorConsecutivosMax = contadorConsecutivos
            contadorConsecutivos = 0
        if contadorConsecutivosMax < contadorConsecutivos:
            contadorConsecutivosMax = contadorConsecutivos
    if contadorConsecutivosMax >= 3:
        res = True
    return res

def quien_gano_el_ta_te_ti_facilito (tablero: list[list[str]]) -> int:
    columnas: dict[str,list[str]] = {}
    for fila in tablero:
        n: int = 1
        for posicion in fila:
            columna: str = "columna " + str(n)
            if (columna) in columnas:
                columnas[columna].append(posicion)
            else:
                columnas[columna] = [posicion]
            n += 1
    victoriasX: int = 0
    victoriasO: int = 0
    for columna in columnas.values():
        if ganoX(columna):
            victoriasX += 1
        if ganoO(columna):
            victoriasO += 1
    if victoriasX > victoriasO:
        res = 1
    elif victoriasO > victoriasX:
        res = 2
    elif victoriasX == victoriasO:
        if victoriasO > 0:
            res = 3
        else:
            res = 0
    return res

"""tablero=[['X','','','',''],
         ['O','O','X','X',''],
         ['O','O','X','O',''],
         ['X','X','X','O',''],
         ['X','O','O','X','']]

tablero1=[['X','O','','','','X'],
          ['O','O','X','X','',''],
          ['O','O','X','O','','X'],
          ['X','X','','O','','X'],
          ['X','O','O','X','','X']]

tablero2=[['X','O','','','','X',''],
          ['O','O','X','X','','','O'],
          ['O','O','X','O','','X',''],
          ['X','X','','O','','X','O'],
          ['X','O','O','X','','X','X']]

print (quien_gano_el_ta_te_ti_facilito(tablero))
print (quien_gano_el_ta_te_ti_facilito(tablero1))
print (quien_gano_el_ta_te_ti_facilito(tablero2))"""


#Ej 4 - CUANTOS PALINDROMOS SUFIJOS
def darVuelta(texto: str) -> str:
    nuevoTexto: str = ""
    for elemento in texto:
        nuevoTexto = elemento + nuevoTexto
    return nuevoTexto

def esPalindromo (sufijo: str) -> bool:
    res: bool = False
    if sufijo == darVuelta(sufijo):
        res = True
    return res

def cuantos_sufijos_son_palindromos (texto: str) -> int:
    listaSufijos: list[str] = []
    for i in range (0, len(texto), 1):
        sufijo: str = ""
        for n in range(i, len(texto), 1):
            sufijo = sufijo + texto[n]
        listaSufijos.append(sufijo)
    contadorSufijos: int = 0
    for sufijo in listaSufijos:
        if esPalindromo(sufijo):
            contadorSufijos += 1
    res = contadorSufijos
    return res

"""print(cuantos_sufijos_son_palindromos(" diego "))
print(cuantos_sufijos_son_palindromos("anana"))"""