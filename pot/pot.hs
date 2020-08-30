soln :: [String] -> Integer
soln x = g 0 (f x)
    where   f a = map (\x -> [read (init x) :: Integer, read ([last x]) :: Integer] ) a
            g a [] = a
            g a (y:ys) = g (a + (y !! 0) ^ (y !! 1)) ys
main = do
    line <- getLine
    let n = read line :: Int
    inputs <- mapM (const getLine) [1..n]
    putStrLn $ show (soln inputs)
