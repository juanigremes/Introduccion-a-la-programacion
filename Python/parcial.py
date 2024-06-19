#Ej 1
def salasTerminadas (listaSalas: list[int]) -> int:
    contadorSalasTerminadas: int = 0
    for sala in listaSalas:
        if sala > 0 and sala < 61:
            contadorSalasTerminadas += 1
    return contadorSalasTerminadas

def promedio (listaSalas: list[int]) -> float:
    promedioTotal: float = 0.0
    salasTerminadas: list[int] = []
    for sala in listaSalas:
        if sala > 0 and sala < 61:
            salasTerminadas.append(sala)
    if len(salasTerminadas) == 0:
        promedioTotal = 0.0
    else:
        for tiempo in salasTerminadas:
            promedioTotal += float(tiempo)
        promedioTotal = (promedioTotal / len(salasTerminadas))
    return promedioTotal

def promedio_de_salidas (registro: dict[str,list[int]]) -> dict[str,tuple[int,float]]:
    res: dict[str,tuple[int,float]] = {}
    for persona in registro.keys():
        salasXpromedio: tuple[int,float] = [salasTerminadas(registro[persona]),promedio(registro[persona])]
        res[persona] = tuple(salasXpromedio)
    return res

#Ej 2
def primerTiempoValido (tiempos: list[int]) -> int:
    lista: list[int] = []
    for indice in range (0, len(tiempos), 1):
        if tiempos[indice] != 0:
            lista.append(indice)
    res: int = lista[0]
    return res

def tiempo_mas_rapido (tiempos_salas: list[int]) -> int:
    menorTiempo: int = primerTiempoValido(tiempos_salas)
    for indice in range (0, len(tiempos_salas), 1):
        if tiempos_salas[indice] > 0 and tiempos_salas[indice] < 61:
            if tiempos_salas [indice] < tiempos_salas[menorTiempo]:
                menorTiempo = indice
    return menorTiempo

#Ej 3
def racha_mas_larga (tiempos: list[int]) -> tuple[int,int]:
    contadorVictorias: int = 0
    indiceInicial = primerTiempoValido(tiempos)
    rachaMaxima: int = 0
    for indice in range (0, len(tiempos), 1):
        if tiempos[indice] > 0 and tiempos[indice] < 61:
            contadorVictorias += 1
            if contadorVictorias == 1:
                indiceInicial = indice
        else:
            if contadorVictorias > rachaMaxima:
                rachaMaxima = contadorVictorias
                indiceInicialDeLaRacha = indiceInicial
            contadorVictorias = 0
        if contadorVictorias > rachaMaxima:
                rachaMaxima = contadorVictorias
                indiceInicialDeLaRacha = indiceInicial
    res: tuple[int,int] = tuple([indiceInicialDeLaRacha, indiceInicialDeLaRacha + rachaMaxima - 1])
    return res

#Ej 4
def soloJugoElTercero (listaTiemposPorSala: list[int]) -> bool:
    res: bool = False
    if listaTiemposPorSala[0] == 0 and listaTiemposPorSala[1] == 0 and listaTiemposPorSala[2] != 0 and listaTiemposPorSala[3] == 0:
        res = True
    return res

def escape_en_solitario (amigos_por_salas: list[list[int]]) -> list[int]:
    res: list[int] = []
    for indice in range (0, len(amigos_por_salas), 1):
        salaConLosTiemposDeLosAmigos: list[int] = amigos_por_salas[indice]
        if soloJugoElTercero(salaConLosTiemposDeLosAmigos):
            res.append(indice)
    return res