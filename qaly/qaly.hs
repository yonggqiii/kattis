soln :: [String] -> Double
soln x = h 0 (g(f x))
    where   f a = map (\str -> (words str)) a
            g a = map (\pair -> [read (head pair) :: Double, read (last pair) :: Double]) a
            h a [] = a
            h a (y:ys) = h (a + (y !! 0) * (y !! 1)) ys

main = do
    line <- getLine
    let n = read line :: Int
    inputs <- mapM (const getLine) [1..n]
    putStrLn $ show (soln inputs)

