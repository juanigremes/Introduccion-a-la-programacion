#Ej 1 - CODIGOS FILTRADOS
def identificarUltimosTres (codigo: int) -> int:
    codigoEnString: str = str(codigo)
    ultimosTres: str = ""
    for i in range (len(codigoEnString)-3,len(codigoEnString),1):
        ultimosTres = ultimosTres + (codigoEnString[i])
    ultimosTres:int = int(ultimosTres)
    return ultimosTres

'''
print(identificarUltimosTres(8734284000))
print(identificarUltimosTres(8734284001))
print(identificarUltimosTres(8734284012))
print(identificarUltimosTres(8734284123))
'''

def cantidadDEdivisores(numero: int) -> list[int]:
    cantDivisores: int = 1
    for n in range (1, numero, 1):
        if numero%n == 0:
            cantDivisores += 1
    return cantDivisores

#print(divisores(2))

def esPrimo (numero: int) -> bool:
    res: bool = True
    if (numero == 0) or (numero == 1) or (cantidadDEdivisores(numero) > 2):
        res = False
    return res

def filtrar_codigos_primos (codigos_barra: list[int]) -> list[int]:
    res: list[int] = []
    for codigo in codigos_barra:
        ultimosTresNumeros: int = identificarUltimosTres(codigo)
        if esPrimo(ultimosTresNumeros):
            res.append(codigo)
    return res

#print(filtrar_codigos_primos([8734284000,12873621002,56371235011,1273921837101,636512783621232]))

#Ej 2 - CAMBIOS DE STOCK
def stock_productos (stock_cambios: list[tuple[str,int]]) -> dict[str,tuple[int,int]]:
    res: dict[str,tuple[int,int]] = {}
    for tupla in stock_cambios:
        producto: str = tupla[0]
        nuevoValor: int = tupla[1]
        if producto in res.keys():
            mayorYmenor: tuple[int,int] = res[producto]
            mayor: int = mayorYmenor[1]
            menor: int = mayorYmenor[0]
            if nuevoValor < menor:
                res[producto] = [nuevoValor,mayor]
            elif nuevoValor > mayor:
                res[producto] = [menor,nuevoValor]
        else:
            res[producto] = [nuevoValor,nuevoValor]
    return res

#print (stock_productos([["manzana",10],["pera",20],["libro",35],["manzana",30],["pera",50],["libro",75],["lapiz",0],["manzana",15],["pera",25],["libro",40],["pipeta",123]]))

#Ej 3 - MATRIZ DE RESPONSABLES
def responsable_por_turno (grilla_horaria: list[list[str]]) -> list[tuple[bool,bool]]:
    semana: dict[str,list[str]] = {}
    for rangoHorario in grilla_horaria:
        n: int = 1
        for persona in rangoHorario:
            dias: str = "dia " + str(n)
            if (dias) in semana:
                semana[dias].append(persona)
            else:
                semana[dias] = [persona]
            n += 1
    res: list[tuple[bool,bool]] = []
    for rotacion in semana.values():
        tuplaMananaTarde: tuple[bool,bool] = [False,False]
        if rotacion[0] == rotacion[1] == rotacion[2] == rotacion[3]:
            tuplaMananaTarde[0] = True
        if rotacion[4] == rotacion[5] == rotacion[6] == rotacion[7]:
            tuplaMananaTarde[1] = True
        res.append(tuplaMananaTarde)
    return res

'''
print (responsable_por_turno([["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"]]))
print (responsable_por_turno([["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["h","i","j","k","l","m","n"],["h","i","j","t","l","m","n"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"]]))
print (responsable_por_turno([["a","b","g"],["a","t","c"],["a","b","g"],["a","f","g"],["l","m","n"],["h","i","j",],["h","i","n"],["h","m","n"]]))
print (responsable_por_turno([["a","b","c","d","e","f","g"],["a","t","c","d","e","f","g"],["a","b","c","d","e","f","g"],["a","b","c","d","e","f","g"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"],["h","i","j","k","l","m","n"]]))
'''

#Ej 4 - SUBSECUENCIA MAS LARGA
def subsecuencia_mas_larga (tipos_pacientes_atendidos: list[str]) -> int:
    res: int = 0
    contadorDeApariciones: int = 0
    contadorDeAparicionesMaximo: int = 0
    for indice in range (0, len(tipos_pacientes_atendidos), 1):
        if tipos_pacientes_atendidos[indice] == "perro" or tipos_pacientes_atendidos[indice] == "gato":
            contadorDeApariciones += 1
            if contadorDeApariciones == 1:
                indicePlaceHolder = indice
        else:
            if contadorDeApariciones > contadorDeAparicionesMaximo:
                res = indicePlaceHolder
                contadorDeAparicionesMaximo = contadorDeApariciones
            contadorDeApariciones = 0
        if contadorDeApariciones > contadorDeAparicionesMaximo:
            res = indicePlaceHolder
            contadorDeAparicionesMaximo = contadorDeApariciones
    return res

'''
print(subsecuencia_mas_larga(["mono","gato","conejo","perro","perro","perro","mono","gato","gato","gato","mono","perro"]))
print(subsecuencia_mas_larga(["mono","gato","conejo","perro","perro","perro","mono","gato","gato","gato","gato","mono","perro"]))
print(subsecuencia_mas_larga(["mono","gato","conejo","perro","perro","perro","mono","mono","perro","gato","gato","gato",]))
'''