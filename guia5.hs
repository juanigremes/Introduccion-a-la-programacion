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
capicua  :: (Eq t) => [t] -> Bool
capicua (x:xs) 
