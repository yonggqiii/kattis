elem' :: (Eq a) => a -> [a] -> Bool
elem' _ [] = False
elem' e (h:t) = if e == h then True else elem' e t

nub :: (Eq a) => [a] -> [a]
nub [] = []
nub (h:t) = if elem' h t then nub t else h : nub t

isAsc :: [Int] -> Bool
isAsc [] = True
isAsc [_] = True
isAsc (h:(x:xs))
    | h > x = False
    | otherwise = isAsc (x:xs)

hasPath :: [(Int, Int)] -> Int -> Int -> Bool
hasPath [] a b = False
hasPath ((x, y):xs) a b
    | a == b    = True
    | x == a    = y == b || hasPath xs y b || hasPath xs a b
    | otherwise = ((hasPath xs a x) && (hasPath xs y b)) || hasPath xs a b

