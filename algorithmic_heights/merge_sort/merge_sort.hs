import System.IO.Unsafe
import Control.Monad
import Data.List.Split


mergeSort :: Ord a => [a] -> [a] -> [a]
mergeSort [] [] = []
mergeSort a [] = a
mergeSort [] a = a
mergeSort (x:xs) (y:ys) | x < y  = x : mergeSort xs (y:ys)
                        | y < x  = y : mergeSort (x:xs) ys
                        | y == x = y : x : mergeSort xs ys

readInt :: String -> Int
readInt = read

arrays = map (map (read :: String -> Int) . words) $ splitOn "\n" $ unsafePerformIO . readFile $ "rosalind_mer.txt"

main = do
        mapM print $ mergeSort (arrays !! 1) (arrays !! 3)
   

