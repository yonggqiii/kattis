main = do
    line <- getLine
    putStrLn ((words line) !! 1)

