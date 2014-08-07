
mergeSort :: Ord a => [a] -> [a] -> [a]
mergeSort [] [] = []
mergeSort a [] = a
mergeSort [] a = a
mergeSort (x:xs) (y:ys) | x < y  = x : mergeSort xs (y:ys)
                        | y < x  = y : mergeSort (x:xs) ys
                        | y == x = y : x : mergeSort xs ys
