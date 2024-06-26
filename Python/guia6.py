# CADA VEZ QUE DEFINO O CORRIJO ALGO TENGO QUE REINICIAR EL python3
import math

#Ej 1.1
def imprimir_hola_mundo () :
    print ("¡Hola Mundo!")

#Ej 1.2
def imprimir_un_verso () :
     print ("days feel like a perfect length")

#Ej 1.3
def raizDe2 () -> float:
     res: float = round (math.sqrt (2) , 4)
     return res

#print (raizDe2())

#Ej 1.4
def factorial_2 () -> int:
     dos: int = 1
     for n in range (2,0,-1):
          dos = dos * n
     return dos

#print (factorial_2())

#Ej 1.5
def perimetro () -> float :
    return 2 * math.pi

#print (perimetro())

#Ej 2.1
def imprimir_saludo (nombre: str) :
     print ("Hola " + nombre)

#print (imprimir_saludo ("Juan"))

#Ej 2.2
def raiz_cuadrada_de (n:float) -> float:
     res: float = math.sqrt (n)
     return res

#Ej 2.3
def farenheit_a_celcius (t: float) -> float :
     t = t - 32
     t = t * 5
     t = t / 9
     return t

#Ej 2.4
def imprimir_dos_veces (estribillo: str) :
     print (2 * estribillo)

#print (imprimir_dos_veces (   """
#                              I said I fly by the dangerous bend symbol (wait, what? Wait, what?)
#                              Don't hesitate to maybe over compensate
#                              And then by the time I catch in my peripheral (wait, what? Wait, what?)
#                              Don't hesitate to maybe overcompensate)
#                              """ ))

#Ej 2.5           n es multiplo de m
def es_multiplo_de (n:int ,m: int) -> bool :
    res: bool = (n%m) == 0 # el % es como el mod en haskell
    return res

#Ej 2.6
def es_par (n: int) -> bool :
     return es_multiplo_de(n,2)

"""
print (es_par (10))
print (es_par (13))
"""

#Ej 2.7
def cantidad_de_pizzas (comensales: int, min_cantidad_de_porciones: int) -> float:
     cantidadPorcionesTotales: int = comensales * min_cantidad_de_porciones
     if (cantidadPorcionesTotales <= 8) :
          pizzas = 1
     else:
          pizzas = int(cantidadPorcionesTotales / 8) + 1

     return pizzas

"""
print (cantidad_de_pizzas(2,2))
print (cantidad_de_pizzas(2,5))
print (cantidad_de_pizzas(9,2))
"""

#Ej 3.1
def alguno_es_0 (n: float, m: float) -> bool:
     res: bool = False
     if (n == 0):
          res = True
     else:
          if (m == 0):
               res = True
     
     return res

#Ej 3.2
def ambos_son_0 (n: float, m: float) -> bool:
     res: bool = False
     if (n == 0) and (m == 0) :
          res = True
     
     return res

#Ej 3.3
def es_nombre_largo (x: str) -> bool :
        longitudx: int = len(x)
        return longitudx >= 3 and longitudx <= 8

#Ej 3.4
def es_bisiesto (ano: int) -> bool:
     res: bool = False
     if (es_multiplo_de (ano , 400)) or ((es_multiplo_de (ano , 4)) and (not (es_multiplo_de (ano , 10)))) :
          res = True
    
     return res

#Ej 4.1
#si la altura fuera en metros la paso a centimetros
def deMTSaCMS (altura: float) -> float:
     altura = altura * 100
     return altura
#supongamos que la altura entra en centimetros
def peso_pino (altura: float) -> float:
     if (altura < 300):
          peso: float = altura * 3
     else:
          peso = 900 + (2 * (altura - 300))

     return peso

#Ej 4.2
def es_peso_util (peso: float) -> bool:
     res: bool = False
     if (400 < peso < 1000 ) :
          res = True
     return res

#Ej 4.3
def sirve_pino (altura: float) -> bool:
     res: bool = False
     if (es_peso_util (peso_pino(altura))):
          res = True
     return res

# EN REALIDAD TENGO QUE VER COMO FUNCIONAN LAS FUNCIONES DE MIN Y MAX

#Ej 5.1
def devolver_el_doble_si_es_par (n:int) -> int :
     if (n%2 == 0):
          return 2*n
     else:
          return n
     
#Ej 5.2
def devolver_valor_si_es_par_sino_el_que_sigue (n:int) -> int:
     if (n%2 == 0):
          return n
     else:
          return (n + 1)
     
#Ej 5.3
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9 (n: int) -> int :
     res: int = n
     if (es_multiplo_de (n,3)):
          res = 2 * n
          if (es_multiplo_de (n,9)):
               res = 3 * n
     return n

#Ej 5.4
def lindo_nombre (nombre: str):
     if (len(nombre) >= 5):
          print ("Tu nombre tiene muchas letras!")
     else:
          print("Tu nombre tiene menos de 5 caracteres")

#print (lindo_nombre("Karen"))
#print (lindo_nombre("Juan"))

#Ej 5.5
def elRango (n: int):
     if (n < 5):
          print ("Menor a 5")
     elif (10 <= n <= 20):
          print ("Entre 10 y 20")
     elif (n > 20):
          print ("Mayor a 20")
     else:
          print ("no me especificaron que hacer aca")

"""
print (elRango (3))
print (elRango (7))
print (elRango (13))
print (elRango (23))
"""

#Ej 5.6
def vacacionesOtrabajo (sexo: str, edad: int) -> str :
     vacaciones: str = "Andá de vacaciones"
     trabajo: str = "Te toca trabajar"
     if (18 < edad < 60):
          print (trabajo)
     else:
          if (60 <= edad < 65):
               if (sexo == "M"):
                    print (trabajo)
               else:
                    print (vacaciones)
          else:
               print (vacaciones)

"""
print (vacacionesOtrabajo ("F",54))
print (vacacionesOtrabajo ("F",63))
"""

#Ej 6.1
def numerosDel1al10 () -> int:
     x: int = 1
     while (x <= 10):
          print (x)
          x += 1

#print (numerosDel1al10())

#Ej 6.2
def paresDel10al40 () -> int :
     x = 10
     while (x <= 40):
          print (x)
          x += 2

#Ej 6.3
def imprimoEco10Veces () -> str:
     x: int = 1
     while (x <= 10):
          print ("eco")
          x += 1

#print (imprimoEco10Veces())

#Ej 6.4
def cuentaRegresiva (x: int) :
    while (x >= 1) :
          print (x)
          x -= 1
    print ("Despegue")

#Ej 6.5
def viajeTiempo (partida: int, llegada: int) :
     while (partida > llegada):
          partida = (partida - 1)
          print ("Viajó un año al pasado, estamos en el año: " + str(partida))
     

#print (viajeTiempo (2020,2015))

#Ej 6.6
def viajeAl384ac (partida: int) :
     llegada: int = 384
     while (partida > (llegada + 19)):
          partida = (partida - 20)
          print ("Viajó veinte años al pasado, estamos en el año: " + str(partida))

#print (viajeAl384ac (2005))

#Ej 7.1
def numerosDel1al10v7 () -> int:
     for num in range (1,11,1):
          print (num)

#Ej 7.2
def paresDel10al40v7 () -> int :
     for num in range (10,42,2) :
          print (num)

#Ej 7.3
def imprimoEco10Vecesv7 () -> str:
     for num in range (1,11,1):
          print ("eco")

#Ej 7.4
def cuentaRegresivav7 (x: int) :
     for num in range (x,0,(-1)) :
          print (num)

     print ("Despegue")

#Ej 7.5
def viajeTiempo (partida: int, llegada: int) :
     for num in range (partida,(llegada+1),(-1)):
          print ("Viajó un año al pasado, estamos en el año: " + str(num))

#Ej 7.6
def viajeTiempo (partida: int) :
     for num in range (partida,(384),(-20)):
          print ("Viajó un año al pasado, estamos en el año: " + str(num))
