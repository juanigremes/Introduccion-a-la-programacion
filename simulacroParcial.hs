-- ejercicio 1 --
relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas xs = (compararTuplas xs) && (verificarValidezTuplas xs)

verificarValidezTuplas :: [(String, String)] -> Bool
verificarValidezTuplas [x] = compararElementosTuplas x
verificarValidezTuplas (x:xs)   | (compararElementosTuplas x == True) = verificarValidezTuplas xs
                                | otherwise = False

compararElementosTuplas :: (String, String) -> Bool
compararElementosTuplas (a,b)   | a == b = False
                                | otherwise = True

compararTuplas :: [(String, String)] -> Bool
compararTuplas [x] = True
compararTuplas (x:y:xs) | (fst x == fst y) && (snd x == snd y) = False
                        | (fst x == snd y) && (snd x == fst y) = False
                        | otherwise = compararTuplas (x:xs) && compararTuplas (y:xs)

-- ejercicio 2 --
personasSinRepetir :: [(String, String)] -> [String]
personasSinRepetir [] = []
personasSinRepetir xs = repetirNVeces (longitud (personas xs)) (personas xs)

longitud :: [String] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs

repetirNVeces :: Int -> [String] -> [String]
repetirNVeces 0 xs = []
repetirNVeces n xs  | n == 1 = sacarPersonasRepetidas xs
                    | otherwise = repetirNVeces (n-1) (sacarPersonasRepetidas xs)

sacarPersonasRepetidas :: [String] -> [String]
sacarPersonasRepetidas [] = []
sacarPersonasRepetidas [x] = [x]
sacarPersonasRepetidas (x:y:xs) | x == y = sacarPersonasRepetidas (x:xs)
                                | otherwise = y: sacarPersonasRepetidas (x:xs) 

personas :: [(String, String)] -> [String]
personas [] = []
personas (x:xs) = (separarPrimerElementoTuplas x) : (separarSegundoElementoTuplas x) : (personas xs)

separarPrimerElementoTuplas :: (String, String) -> String
separarPrimerElementoTuplas (a,b) = fst (a,b) 

separarSegundoElementoTuplas :: (String, String) -> String
separarSegundoElementoTuplas (a,b) = snd (a,b) 


-- ejercicio 3 --
amigosDe :: String -> [(String, String)] -> [String]
amigosDe p (x:xs) = eliminarPersonaPrincipal p (personas (verificoPertenencia p (x:xs)))

verificoPertenencia :: String -> [(String, String)] -> [(String, String)] 
verificoPertenencia p [] = [] 
verificoPertenencia p (x:xs)    | (pertenece p x == True) = x : (verificoPertenencia p xs)
                                | otherwise = (verificoPertenencia p xs)

pertenece :: String -> (String, String) -> Bool
pertenece p (a,b)   | (p == a || p == b ) = True
                    | otherwise = False

eliminarPersonaPrincipal :: String -> [String] -> [String]
eliminarPersonaPrincipal _ [] = []
eliminarPersonaPrincipal p (x:xs)   | p == x = eliminarPersonaPrincipal p xs
                                    | otherwise = x: eliminarPersonaPrincipal p xs

-- ejercicio 4 --
personaConMasAmigos :: [(String, String)] -> String
personaConMasAmigos xs = compararContadores (personas xs)


compararContadores :: [String] -> String
compararContadores [x] = x
compararContadores (x:y:xs) | (contadorDeApariciones x (x:y:xs)) >= (contadorDeApariciones y (x:y:xs)) = compararContadores (x:xs)
                            | otherwise = compararContadores (y:xs)

contadorDeApariciones :: String -> [String] -> Int
contadorDeApariciones _ [] = 0
contadorDeApariciones p (x:xs)  | p == x = 1 + contadorDeApariciones p xs
                                | otherwise = contadorDeApariciones p xs