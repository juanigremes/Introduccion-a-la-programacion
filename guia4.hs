-- 1)
fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
           | n == 1 = 1
           | otherwise = fibonacci (n - 1) + fibonacci (n - 2)


-- 2)
parteEntera :: Float -> Int
parteEntera x   | x >= 0 && x < 1 = 0
               | x < 0 = (parteEntera (x + 1) ) - 1
               | otherwise = (parteEntera (x - 1)) + 1


-- 3)
esDivisible :: Int -> Int -> Bool
esDivisible x y | ((x - y) == 0) = True
               | ((x - y) < y) = False
               | otherwise = esDivisible (x - y) y
-- otra resolucion
-- esDivisible x y  | x < y = x == 0
--                  | otherwise esDivisible (x-y) y


-- 4)
sumaImpares :: Int -> Int
sumaImpares n   | n==1 = 1
                | otherwise = n + (n-1) + sumaImpares (n-1)


-- 5)
medioFact :: Int -> Int
medioFact n | n==1 = 1
            | n==0 = 1
            | otherwise =  medioFact (n-2) * n


-- 6)
sumaDigitos :: Int -> Int
sumaDigitos n   | n < 10 = n
                | otherwise = mod n 10 + sumaDigitos (div n 10)


-- 7) 
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n   | n < 10 = True
                        | otherwise = mod n 10 == mod (div n 10) 10 && todosDigitosIguales (div n 10)



-- 8) no lo entendi del todo
iesimoDigito :: Int -> Int -> Int
iesimoDigito n i    | n < 10 = n 
                    | otherwise = (n `div` 10^(cantDigitos n-i)) `mod` 10

cantDigitos :: Int -> Int
cantDigitos n | n < 0 = undefined
              | n == 0 = 1
              | otherwise = aux8 (n `div` 10)

aux8 :: Int -> Int
aux8 0 = 1
aux8 n = 1 + aux8 (n `div` 10)


-- 9) tampoco lo entendi muy bien
esCapicua :: Int -> Bool
esCapicua n | n < 10 = True
            | otherwise = aux9 n 1

aux9 :: Int -> Int -> Bool
aux9 n posCifra | posCifraOpuesta == posCifra = True
                | posCifra > posCifraOpuesta = True
                | otherwise = aux9 n (posCifra+1) && (iesimoDigito n posCifra == iesimoDigito n posCifraOpuesta)
                where   nDig= cantDigitos n
                        posCifraOpuesta = nDig - posCifra + 1


-- 10)
-- a)
f1 :: Int -> Int
f1 n    | n==0 = 1
        | otherwise = 2^(n) + f1 (n-1)

-- b)
f2 :: Int -> Float -> Float
f2 n q  | n==0 = 0
        | otherwise = qnVeces n q + f2 (n-1) q

qnVeces :: Int -> Float -> Float
qnVeces n q | n==1 = q 
            | otherwise = q * qnVeces (n-1) q

-- c) 
f3 :: Int -> Float -> Float
f3 n q = f2 (n*2) q
-- f3 n = f2 (n*2) -> funcion currificada

-- d)
f4 :: Int -> Float -> Float
f4 n q = (f2 (n*2) q) - (f2 n q) + (q^n)


-- 11)
eAprox :: Int -> Float
eAprox n    | n==0 = 1
            | otherwise = eAprox (n-1) + (1 / fromIntegral(factorial n))

factorial :: Int -> Int
factorial n | n==0 = 1
            | otherwise = factorial (n-1) * n
