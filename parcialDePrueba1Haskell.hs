-- Ejercicio 1 --
votosEnBlanco :: [(String , String)] -> [Int] -> Int -> Int
votosEnBlanco f v n     | (sumaTotalDeVotos v) < n = n - sumaTotalDeVotos v
                        | otherwise = 0
                      
sumaTotalDeVotos :: [Int] -> Int
sumaTotalDeVotos [] = 0
sumaTotalDeVotos (x:xs) = x + (sumaTotalDeVotos xs)

-- no se si tengo que tener en cuenta formulas en las que hay algun string vacio, porque entra como formula valida, ya que es "TRUE" y no lo condiciona el asgura de ese problema, pero me suena muy raro que tenga que tenerlo en cuenta.
-- formulasBlancasYSusVotos :: [(String , String)] -> [(String , String)] 
-- formulasBlancasYSusVotos [] = []
-- formulasBlancasYSusVotos (x:xs) | fst x == " " || snd x == " " = x: formulasBlancasYSusVotos xs
--                                 | otherwise = formulasBlancasYSusVotos xs

-- Ejercicio 2 --
formulasValidas :: [(String , String)] -> Bool
formulasValidas [] = False
formulasValidas x = (verificarFormulas x) && (compararFormulas x)

-- verifico que las formulas no tienen nonmbres repetidos en si mismas.
verificarFormulas :: [(String , String)] -> Bool
verificarFormulas [] = True
verificarFormulas (x:xs)    | ((fst x) == (snd x)) = False
                            | otherwise = verificarFormulas xs 

-- comparo las formulas entre si para ver que no haya nadie postulandose por dos partidos diferentes
compararFormulas :: [(String , String)] -> Bool
compararFormulas [] = True
compararFormulas [x] = True
compararFormulas (x:y:xs)   | (fst x) == (fst y) || (fst x) == (snd y) || (snd x) == (fst y) || (snd x) == (snd y) = False
                            | otherwise = compararFormulas (y:xs) && compararFormulas (x:xs)


-- Ejercicio 3 --
porcentajeDeVotos :: String -> [(String , String)] -> [Int] -> Float
porcentajeDeVotos p f v = 100 * (fromIntegral (identificarFormulaYSusVotos p f v)) / (fromIntegral (sumaTotalDeVotos v))

-- como la posicion de los votos en su lista se corresponde con la posicion de la formula asociada puedo hacer lo siguiente:
identificarFormulaYSusVotos :: String -> [(String , String)] -> [Int] -> Int
identificarFormulaYSusVotos p (x:xs) (v:vs) | (p == (fst x)) = v 
                                            | otherwise = identificarFormulaYSusVotos p xs vs


-- Ejercicio 4 --
proximoPresidente :: [(String , String)] -> [Int] -> String
proximoPresidente [f] [v] = fst f
proximoPresidente (x:y:fs) (v:w:vs) | v > w = proximoPresidente (x:fs) (v:vs)
                                    | otherwise = proximoPresidente (y:fs) (w:vs)