-- 1)
-- 1-
longitud :: [t] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

-- 2-
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs)   | longitud (xs) == 0 = x
                | otherwise = ultimo xs

-- 3-
principio :: [t] -> [t]
--principio [x] = []
--principio (x:xs) = x: principio xs
principio xs    | longitud xs == 1 = []
                | otherwise = (head xs) : principio (tail xs)

-- 4-
reverso :: [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x] 


-- 2)
-- 1-
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece a xs      | a == (head xs) = True
                    | otherwise = pertenece a (tail xs)
--pertenece x (y:ys) = (x==y || pertenece x ys) && ys/=[]

-- 2-
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) = x==y && todosIguales (y:xs)

-- 3-
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (x:y:xs) = x/=y && (todosDistintos (x:xs) && todosDistintos (y:xs))

-- 4-
opuesto :: Bool -> Bool
opuesto True = False
opuesto False = True

hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos x =  opuesto (todosDistintos x)

-- 5-
quitar :: (Eq t) => t -> [t] -> [t]
quitar a (x:xs) | pertenece a xs = quitarAux a (x:xs)
                | otherwise = x:xs
                
quitarAux :: (Eq t) => t -> [t] -> [t]
quitarAux a (x:xs)  | a==x = xs
                    | otherwise = x: quitarAux a xs

-- 6-
quitarTodos :: (Eq t ) => t -> [t] -> [t]
quitarTodos a (x:xs)    | pertenece a xs = quitarTodosAux a (x:xs)
                        | otherwise = x:xs 

quitarTodosAux :: (Eq t) => t -> [t] -> [t]
quitarTodosAux a (x:xs) | a==x && xs==[] = []
                        | a/=x && xs==[] = x:xs
                        | a==x = quitarTodosAux a xs
                        | otherwise = x: quitarTodosAux a xs

-- 7-
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
--eliminarRepetidos (x:y:xs)  | x==y = eliminarRepetidos (y:xs)  esto no me servia si habia repetidos desordenados, solo si estaban pegados.
--                            | otherwise = x: eliminarRepetidos (y:xs)
eliminarRepetidos (x:xs)    | pertenece x xs == True = eliminarRepetidos xs
                            | otherwise = x: eliminarRepetidos xs -- esto me sirve pero deja toda la lista desordenada.

-- 8-
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos [] (y:ys) = False
mismosElementos (x:xs) [] = False
mismosElementos [x] [y] | x==y =True
                        | otherwise = False
mismosElementos (x:xs) (y:ys) = mismosElementosAux (x:xs) (y:ys) && mismosElementosAux (y:ys) (x:xs)

mismosElementosAux :: (Eq t) => [t] -> [t] -> Bool
mismosElementosAux [] (y:ys) = True
mismosElementosAux (x:xs) (y:ys)   | pertenece x (y:ys) == True = mismosElementosAux xs (y:ys)
                                   | otherwise = False

-- 9-
capicua :: (Eq t) => [t] -> Bool
capicua [] = True
capicua [x] = True
capicua (x:xs)  | (x) == (head (reverso (x:xs))) = capicua (eliminarPyU (x:xs))
                | otherwise = False
                where eliminarPyU (x:xs) = tail (reverso xs) -- podria meterlo directamente sin usar where pero lo pongo para entender que estoy haciendo.


-- 3
-- 1-
sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

-- 2-
productoria :: [Int] -> Int
productoria [] = 0
productoria [x] = x
productoria (x:xs) = x * productoria xs

-- 3-
maximo :: [Int] -> Int
maximo [] = 0
maximo [x] = x
maximo (x:y:xs) | x >= y = maximo (x:xs)
                | otherwise = maximo (y:xs)

-- 4-
sumarN :: Int -> [Int] -> [Int]
sumarN n [] = []
sumarN n [x] = [x + n]
sumarN n (x:xs) = (x + n) : sumarN n xs

-- 5-
sumarElPrimero :: [Int] -> [Int]
sumarElPrimero (x:xs) = sumarN x (x:xs) 

-- 6-
sumarElUltimo :: [Int] -> [Int]
sumarElUltimo (x:xs) = sumarN (head (reverso (x:xs))) (x:xs)
-- tambien tengo la funcion ultimo pero me habia olvidado -- 

-- 7-
pares :: [Int] -> [Int]
pares [] = []
pares [x]   | mod x 2 == 0 = [x]
            | otherwise = []
pares (x:xs)    | mod x 2 == 0 = x: pares xs
                | otherwise = pares xs

-- 8-
multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN n [] = []
multiplosDeN n [x]  | mod x n == 0 = [x]
                    | otherwise = []
multiplosDeN n (x:xs)   | mod x 2 == 0 = x: multiplosDeN n xs
                        | otherwise = multiplosDeN n xs

-- 9- 
ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs)  | verificarOrden (x:xs) == True = (x:xs)
                | otherwise = ordenar (quitar (maximo (x:xs)) (x:xs)) ++ [(maximo (x:xs))]

verificarOrden :: [Int] -> Bool
verificarOrden [] = True
verificarOrden [x] = True
verificarOrden (x:y:xs) | x <= y = verificarOrden (y:xs)
                        | otherwise = False


-- 4
-- a-
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] = [x]
sacarBlancosRepetidos (x:y:xs)  | (x == ' ') &&  (x == y) = sacarBlancosRepetidos (x:xs)
                                | otherwise = x: sacarBlancosRepetidos (y:xs)

-- b-
contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras [x]  | (x == ' ') = 0
                    | otherwise = 1 
contarPalabras (x:xs) = 1 + contarBlancos (sacarBlancoPyU (sacarBlancosRepetidos (x:xs)))

sacarBlancoPyU :: [Char] -> [Char]
sacarBlancoPyU (x:xs)   | (x == ' ') = sacarBlancoUltimo (reverso xs)
                        | otherwise = sacarBlancoUltimo (reverso (x:xs))

sacarBlancoUltimo :: [Char] -> [Char]
sacarBlancoUltimo (x:xs)    | (x == ' ') = reverso xs
                            | otherwise = reverso (x:xs)

contarBlancos :: [Char] -> Int
contarBlancos [] = 0
contarBlancos (x:xs)    | (x == ' ') = 1 + contarBlancos xs
                        | otherwise = contarBlancos xs

-- c- NO ENTIENDO LA FORMA DE TRABAJAR CON TUPLAS Y SECUENCIAS
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras [x] = [[x]]
palabras (x:xs) = juntarPalabras(sacarBlancoPyU(sacarBlancosRepetidos (x:xs)))
                

juntarPalabras :: [Char] -> [[Char]]
juntarPalabras [] = []
--juntarPalabras [x] = [[x]]
juntarPalabras (x:xs) = fst (juntarLetras (x:xs)) : juntarPalabras (snd (juntarLetras (x:xs)))

juntarLetras :: [Char] -> ([Char] , [Char])
juntarLetras [x] = ([x] , [])
juntarLetras (x:xs) | (x == ' ') = ([] , xs)
                    | otherwise = (x:fst (juntarLetras xs) , snd (juntarLetras xs))

-- d-
palabraMasLarga :: [Char] -> [Char]
palabraMasLarga xs = compararLongitud (palabras xs) 

compararLongitud :: [[Char]] -> [Char]
compararLongitud [] = []
compararLongitud [x]= x
compararLongitud (x:y:xss)  | (longitud x) >= (longitud y) = compararLongitud (x:xss) 
                            | otherwise = compararLongitud (y:xss)

-- e-
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar [x] = x
aplanar (x:xs) = x ++ (aplanar xs)

-- f- 
aplanarConBlancos :: [[Char]] -> [Char]
aplanarConBlancos [] = []
aplanarConBlancos [x] = x
aplanarConBlancos (x:xs) = x ++ [' '] ++ (aplanarConBlancos xs)

-- g-
aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos [] _ = []
aplanarConNBlancos [x] _ = x
aplanarConNBlancos (x:xs) n = x ++ (agregarNBlancos n) ++ (aplanarConNBlancos xs n)

agregarNBlancos :: Int -> [Char]
agregarNBlancos 0 = []
agregarNBlancos 1 = [' ']
agregarNBlancos n = ' ' : (agregarNBlancos (n-1))


-- 5
-- 1-
sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada xs = revierto (sumaAcumuladaRevertida (revierto xs))

revierto :: (Num t) => [t] -> [t]
revierto [] = []
revierto (x:xs) = revierto xs ++ [x] 

sumaAcumuladaRevertida :: (Num t) => [t] -> [t]
sumaAcumuladaRevertida [] = []
sumaAcumuladaRevertida (x:xs) = sumaElementos (x:xs) : sumaAcumuladaRevertida xs

sumaElementos :: (Num t) => [t] -> t
sumaElementos [] = 0
sumaElementos (x:xs) = x + sumaElementos xs

-- 2-
descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = [[]]
descomponerEnPrimos [x] = [verificoQueEsPrimo x]
descomponerEnPrimos (x:xs) = (verificoQueEsPrimo x) : (descomponerEnPrimos xs)

verificoQueEsPrimo :: Int -> [Int]
verificoQueEsPrimo x    | esPrimo x = [x]
                        | otherwise = descompongo x 2

--en descompongo divido por primos--
descompongo :: Int -> Int -> [Int]
descompongo x n | mod x n == 0 = n : verificoQueEsPrimo (div x n)
                | otherwise = descompongo x (siguientePrimo (n+1))

siguientePrimo ::  Int -> Int
siguientePrimo n    | esPrimo n == True = n
                    | otherwise = siguientePrimo (n+1)

esPrimo :: Int -> Bool
esPrimo x   | x==1 = False 
            | otherwise = menorDivisor x == x

menorDivisor :: Int -> Int
menorDivisor n  | mod n 2 == 0 = 2
                | n==1 = 1
                | otherwise = divisorImpares n 3

divisorImpares :: Int -> Int -> Int
divisorImpares n x  | mod n x == 0 = x
                    | otherwise = divisorImpares n (x+2)
