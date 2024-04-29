doubleMe x = x + x

-- 1)
-- a)
f :: Int -> Int
f 1 = 8
f 4 = 131
f 16 = 16

-- b)
g :: Int -> Int
g 8 = 16
g 16 = 4
g 131 = 1

-- c)
h :: Int -> Int
h x = f (g x)

k :: Int -> Int
k x = g (f x)

-- 2)
-- a)
-- problema absoluto (x : Z) : Z {
-- requiere: (True)
-- asegura: (res es el valor absoluto de x)
-- }

absoluto :: Int -> Int
absoluto x = abs(x)


-- b)
-- problema maximoAbsoluto (x,y : Z) : Z {
-- requiere: (True)
-- asegura: (res es el valor absoluto del numero mas alto)
-- }

maximoAbsoluto :: Int -> Int -> Int
maximoAbsoluto x y  | (abs x > abs y || abs x == abs y) = abs x
                    | abs y > abs x = y


-- c)
-- problema maximo3 (x,y,z : Z) : Z {
-- requiere: (True)
-- asegura: (res es el valor absoluto del numero mas alto)
-- }

maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z   | (maximoAbsoluto x y) > z || (maximoAbsoluto x y) == z = (maximoAbsoluto x y)
                | z > (maximoAbsoluto x y) = z 



-- d)
-- problema algunoEs0 (x,y : Q) : Bool {
-- requiere: (True)
-- asegura: (res es True solamente si algun numero es 0)
-- }

algunoEs0 :: Float -> Float -> Bool
algunoEs0 x y   | (x == 0) || (y == 0) = True
                | otherwise = False

algunoEs02 :: Float -> Float -> Bool
algunoEs02 _ 0 = True
algunoEs02 0 _ = True
algunoEs02 x y = False


-- e)
-- problema ambosSon0 (x,y : Q) : Bool {
-- requiere: (True)
-- asegura: (res es True solamente si ambos numeros son 0)
-- }

ambosSon0 :: Float -> Float -> Bool
ambosSon0 x y   | (x == 0 && y == 0) = True
                | otherwise = False

ambosSon02 :: Float -> Float -> Bool
ambosSon02 0 0 = True
ambosSon02 x y = False


-- f)
-- problema mismoIntervalo (x,y : R) : Bool {
-- requiere: (True)
-- asegura: (res es True solamente si ambos numeros pertenecen al mismo intervalo -> intervalos a tener en cuenta:(−∞, 3],(3, 7] y (7, ∞))
-- }

mismoIntervalo :: Float -> Float -> Bool
mismoIntervalo x y  | ((x < 3 || x == 3) && (y < 3 || y == 3)) = True
                    | (((x > 3) && (x < 7 || x == 7)) && ((y > 3) && (y < 7 || y ==7))) = True
                    | (x > 7 && y > 7) = True
                    | otherwise = False


-- g)
-- problema sumaDistintos (x,y,z : Z) : Z {
-- requiere: (true)
-- asegura: (res es el resultado de la suma de los numeros que no esten repetidos)
-- }

suma :: Int -> Int -> Int
suma a b | a /= b = a + b
            | a==b = a

sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x /= z) && (y /= z) = (suma x y) + z
                    | (x == z) || (y == z) = suma x y


-- h)
-- problema esMultiploDe (x,y : N) : Bool {
-- requiere: (true)
-- asegura: (res es True solamente si el primer numero es multiplo del segundo)
-- }

esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y    | mod x y == 0 = True
                    | otherwise = False


-- i)        
-- problema digitoUnidades (x : Z) : Z {
-- requiere: (true)
-- asegura: (res es el digito de las unidades)
-- }

digitoUnidades :: Int -> Int
digitoUnidades x = x `mod` 10


-- j)
-- problema digitoDecenas (x : Z) : Z {
-- requiere: (true)
-- asegura: (res es el digito de las decenas)
-- }

digitoDecenas :: Int -> Int
digitoDecenas x = (x `mod` 100) `div` 10


-- 3)
-- problema estanRelacionados (a:Z, b:Z) : Bool {
-- requiere: {a ̸= 0 ∧ b ̸= 0}
-- asegura: {(res = true) ↔ a ∗ a + a ∗ b ∗ k = 0 para alg´un k ∈ Z con k ̸= 0)}
-- }

estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b   | mod (a*a) (a*b) == 0 = True
                        | otherwise = False


-- 4)
-- a)
-- problema prodInt (tupla1, tupla2 :Float X Float) : R {
-- requiere: (True)
-- asegura: (res es el producto interno entre las dos tuplas)
-- }


prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt (x,y) (a,b) = x * a + y * b




-- b)
-- problema todoMenor (tupla1, tupla2 :Float X Float) : Bool {
-- requiere: (True)
-- asegura: (res es True solamente si cada uno de los elementos de la pimera tupla es estrictamente menor a los elementos correspondientes (que esten en la misma posicion) de la segunda)
-- }


todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor (x,y) (a,b)   | (x < a) && (y < b) = True
                       | otherwise = False




-- c)
-- problema distanciaPuntos (tupla1, tupla2 :Float X Float) : Float {
-- requiere: (True)
-- asegura: (res es la distancia entre los dos puntos, a tener en centa esta formula: √((x2 - x1)² + (y2 - y1)²))
-- }


distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (x,y) (a,b) = sqrt(((a-x)**2)+((b-y)**2))




-- d)
-- problema sumaTerna (terna : Float X Float x Float) : Float {
-- requiere: (True)
-- asegura: (res es la suma de los tres elementos de la terna)
-- }


sumaTerna :: (Float,Float,Float) -> Float
sumaTerna (x,y,z) = x + y + z




-- e)
-- problema sumarSoloMultiplos (terna : (Z X Z x Z), n : (N)) : Z {
-- requiere: (True)
-- asegura: (res es la suma de los elementos de la terna que sean multiplos del numero natural)
-- }

multZN :: Int -> Int -> Int
multZN z n  | (esMultiploDe z n) == True = z
           | otherwise = 0


multYN :: Int -> Int -> Int -> Int
multYN y z n    | (esMultiploDe y n) == True = y + multZN z n
               | otherwise = multZN z n


sumarSoloMultiplos :: (Int,Int,Int) -> Int -> Int
sumarSoloMultiplos (x,y,z) n    | (esMultiploDe x n == True) = x + (multYN y z n)
                               | otherwise = multYN y z n




-- f)
-- problema posPrimerPar (terna :(Z X Z x Z) ) : Z {
-- requiere: (True)
-- asegura: (res es la posicion del primer numero par)
-- asegura: (si no hay numero par, res es 4)
-- }


posPrimerPar :: (Int,Int,Int) -> Int
posPrimerPar (x,y,z)    | mod x 2 == 0 = 1
                       | mod y 2 == 0 = 2
                       | mod z 2 == 0 = 3
                       | otherwise =4




-- g)


crearPar :: a -> b -> (a,b)
crearPar a b = (a,b)


-- h)


invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)


-- 5)


-- problema todosMenores (t : Z × Z × Z) : Bool {
-- requiere: {True}
-- asegura: {(res = true) ↔ ((f (t0) > g(t0)) ∧ (f (t1) > g(t1)) ∧ (f (t2) > g(t2)))}
-- }


-- problema f (n: Z) : Z {
-- requiere: {T rue}
-- asegura: {(n ≤ 7 → res = n2) ∧ (n > 7 → res = 2n − 1)}
-- }

-- problema g (n: Z) : Z {
-- requiere: {T rue}
-- asegura: {Si n es un n´umero par, entonces res = n/2, en caso contrario, res = 3n + 1}
-- }

todosMenores :: (Int,Int,Int) -> Bool
todosMenores (x,y,z)    | ((f5 x) > (g5 x)) && ((f5 y) > (g5 y)) && ((f5 z) > (g5 z)) = True
                       | otherwise = False

f5 :: Int -> Int
f5 n    | n <= 7 = n*2
       | otherwise = (2*n) - 1

g5 :: Int -> Int
g5 n    | mod n 2 == 0 = div n 2
       | otherwise = (3*n) + 1


-- 6)
-- problema bisiesto (ano: Z) : Bool {
-- requiere: {True}
-- asegura: {res = False ↔ ano no es multiplo de 4 o ano es multiplo de 100 pero no de 400}
-- }

bisiesto :: Int -> Bool
bisiesto x    | (mod x 4 /= 0) = False
              | (mod x 100 == 0) && (mod x 400 /= 0) = False
              | otherwise = True


-- 7)
-- problema distanciaManhattan (p : R × R × R, q : R × R × R) : R {
-- requiere: {True}
-- asegura: {res = sumatoria (desde i=0 hasta i=2) de  |pi − qi|}
-- }

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x,y,z) (a,b,c) | (x - a) + (y - b) + (z - c) <= 0 = -1 * ((x - a) + (y - b) + (z - c))
                                   | otherwise = (x - a) + (y - b) + (z - c)


-- 8) 
-- problema comparar (a:Z, b:Z) : Z {
-- requiere: {T rue}
-- asegura: {(res = 1 ↔ sumaUltimosDosDigitos(a) < sumaUltimosDosDigitos(b))}
-- asegura: {(res = −1 ↔ sumaUltimosDosDigitos(a) > sumaUltimosDosDigitos(b))}
-- asegura: {(res = 0 ↔ sumaUltimosDosDigitos(a) = sumaUltimosDosDigitos(b))}
-- }
-- problema sumaUltimosDosDigitos (x: Z) : Z {
-- requiere: {True}
-- asegura: {res = (|x| mod 10) + (⌊(|x|/10)⌋ mod 10)}
-- }

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x     | x > 0 = (x `mod` 10) + (x `mod` 100) `div` 10
                            | otherwise = sumaUltimosDosDigitos (-1 * x)

comparar :: Integer -> Integer -> Integer
comparar a b  | ((sumaUltimosDosDigitos a) < (sumaUltimosDosDigitos b)) = 1
              | ((sumaUltimosDosDigitos a) > (sumaUltimosDosDigitos b)) = -1
              | otherwise = 0


-- 9) sii = si y solo si
-- a) f1 recibe un "n" de tipo Float y evalua si es 0 o no, si n es 0 entonces devuelve un 1, de lo contrario devuelve un 0
-- problema f1 (n : R) : R {
-- requiere: {true}
-- asegura: { res = 1 sii n = 0 }
-- asegura: { res = 0 sii n /= 0 }
-- }

-- b) f2 recibe un "n" de tipo Float y evalua si es 1 o -1, si n es 1 entonces devuelve un 15, de lo contrario devuelve un -15
-- problema f2 (n : R) : R {
-- requiere: {n = 1 || n = -1}
-- asegura: { res = 15 sii n = 1 }
-- asegura: { res = -15 sii n = -1 }
-- }

-- c) f3 recibe un "n" de tipo Float y evalua si es menor o igual a 9 o si es mayor o igual a 3, si es la primera entonces devuelve un 7, si es la segunda devuelve un 5
-- problema f3 (n : R) : R {
-- requiere: {true}
-- asegura: { res = 7 si n <= 9 }
-- asegura: { res = 5 si n >= 3 }
-- }

-- d) f4 recibe dos inputs "x y" ambos de tipo Float. Luego calcula el promedio, es decir, los suma y luego deivide el resultado por 2
-- problema f4 (x,y : R) : R {
-- requiere: {true}
-- asegura: { res = (x+y)/2 }
-- }

-- e) f4 recibe dos inputs "x y" ambos de tipo Float, pero en forma de tupla. Luego calcula el promedio, es decir, los suma y luego deivide el resultado por 2
-- problema f4 (t : R x R) : R {
-- requiere: {true}
-- asegura: { res = (x+y)/2 }
-- }

-- f) f5 recibe dos inputs "a b" uno de tipo Float y el otro de tipo Int, para luego devolver el valor de verdad (con un tipo Bool) de una proposicion que incluye otra funcion ya definida "truncate a"
-- problema f5 (a: R , b: Z) : Bool {
-- requiere: {true}
-- asegura: { res = True sii truncate a == b }
-- }
