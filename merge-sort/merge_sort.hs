{-  Mergesort algorithm implementation in Haskell.
    Input: a list of integers in any order. 
    Output: a list with the same intergers ordened by ascending
    Example: 
    > mergeSort [4,1,56,78,42412,45]
    > [1,4,45,56,78,42412]
-}

mergeSort :: [Int] -> [Int]
mergeSort [] = []
mergeSort [h] = [h]
mergeSort l = merge (mergeSort left) (mergeSort right)
              where left = take ((length l) `div` 2) l
                    right = drop ((length l) `div` 2) l

merge :: [Int] -> [Int] -> [Int]
merge x [] = x
merge [] y = y
merge (hx:tlx) (hy:tly) | hx <= hy = hx:merge tlx (hy:tly)
                        | otherwise = hy:merge (hx:tlx) tly