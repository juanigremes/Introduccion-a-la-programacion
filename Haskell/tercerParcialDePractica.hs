-- ejercicio 1 --

porcentajeDeVotosAfirmativos :: [(String,String)] -> [Int] -> Int -> Float
porcentajeDeVotosAfirmativos _ vs t = 100 * (fromIntegral (sumaVotosTotales vs)) / (fromIntegral t)

sumaVotosTotales :: [Int] -> Int
sumaVotosTotales [] = 0
sumaVotosTotales (v:vs) = v + sumaVotosTotales vs


-- ejercicio 2 --

formulasInvalidas :: [(String,String)] -> Bool
formulasInvalidas [] = False
formulasInvalidas fs = (elementosIguales fs) || (comparoTuplas fs)

elementosIguales :: [(String,String)] -> Bool
elementosIguales [] = False
elementosIguales (f:fs) | (fst f) == (snd f) = True
                        | otherwise = elementosIguales fs

comparoTuplas :: [(String,String)] -> Bool
comparoTuplas [] = False
comparoTuplas [x] = False
comparoTuplas (x:y:fs)  | (fst x) == (fst y) || (fst x) == (snd y) || (snd x) == (fst y) || (snd x) == (snd y) = True
                        | otherwise = comparoTuplas (x:fs) || comparoTuplas (y:fs)


-- ejercicio 3 --

porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos x fs vs = 100 * (fromIntegral(identificoViceYSusVotos x fs vs)) / (fromIntegral(sumaVotosTotales vs))

identificoViceYSusVotos :: String -> [(String,String)] -> [Int] -> Int
identificoViceYSusVotos x (f:fs) (v:vs) | (pertenece x f) == True = v
                                        | otherwise = identificoViceYSusVotos x fs vs

pertenece :: String -> (String,String) -> Bool
pertenece x tp  | x == (snd tp) = True
                | otherwise = False


-- ejercicio 4 --

menosVotado :: [(String,String)] -> [Int] -> String
menosVotado [f] _ = fst f
menosVotado (x:y:fs) (v:w:vs)   | v <= w = menosVotado (x:fs) (v:vs)
                                | otherwise = menosVotado (y:fs) (w:vs)


-- Los ejercicios 3 y 4 los puedo hacer asi porque estan en las mismas posiciones los votos correspondientes a cada formula postulada.
