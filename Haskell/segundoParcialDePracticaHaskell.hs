-- ejercicio 1 --

atajaronSuplentes :: [(String,String)] -> [Int] -> Int -> Int
atajaronSuplentes es gs t = t - (sumaTotalDeGoles gs) 

sumaTotalDeGoles :: [Int] -> Int
sumaTotalDeGoles [] = 0
sumaTotalDeGoles [x] = x
sumaTotalDeGoles (x:xs) = x + sumaTotalDeGoles xs


-- ejercicio 2 --

equiposValidos :: [(String,String)] -> Bool
equiposValidos [] = True
equiposValidos x = (arqueroDiferenteDeEquipo x) && (repeticionesEntreTuplas x)
    
arqueroDiferenteDeEquipo :: [(String,String)] -> Bool
arqueroDiferenteDeEquipo [] = True
arqueroDiferenteDeEquipo (x:xs) | sonDiferentesEntreSi x == True = arqueroDiferenteDeEquipo xs
                                | otherwise = False

sonDiferentesEntreSi :: (String,String) -> Bool
sonDiferentesEntreSi (a,b)  | a == b = False
                            | otherwise = True

repeticionesEntreTuplas :: [(String,String)] -> Bool
repeticionesEntreTuplas [] = True
repeticionesEntreTuplas (x:y:xs)    | (fst x == fst y) || (snd x == snd y) = False
                                    | otherwise = repeticionesEntreTuplas (x:xs) && repeticionesEntreTuplas (y:xs)


-- ejercicio 3 --

porcentajeDeGoles :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeGoles a es gs = 100 * (fromIntegral (golesAlArquero a es gs)) / (fromIntegral (sumaTotalDeGoles gs))

golesAlArquero :: String -> [(String,String)] -> [Int] -> Int
golesAlArquero _ [] _ = 0
golesAlArquero a (x:es) (g:gs)  | a == (snd x) = g
                                | otherwise = golesAlArquero a es gs


-- ejercicio 4 --

vallaMenosVencida :: [(String,String)] -> [Int] -> String
vallaMenosVencida (e:es) [g] = (snd e)
vallaMenosVencida (e:c:es) (x:y:gs) | x <= y = vallaMenosVencida (e:es) (x:gs)
                                    | otherwise = vallaMenosVencida (c:es) (y:gs)

