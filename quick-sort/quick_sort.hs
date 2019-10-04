{-  Quick sort algorithm implementation in Haskell.
    Input: a list of integers in any order. 
    Output: a list with the same intergers ordened by ascending
    Example: 
    > quickSort [4,1,56,78,42412,45]
    > [1,4,45,56,78,42412]
-}

{-  
    h : head
    tl : tail
    It receives a list of integers and returns a list of integers.
    If it's an empty list, returns an empty list.
    If the list only has one element, the head, return the list with it.
    If it has more than one element, take the head as the pivot. Use list
    comprehension to put the lesser than or equal elements to the pivot
    on the left list and the greater elements in the right list, calling
    itself recursively on these lists.
-}

quickSort :: [Int] -> [Int]
quickSort [] = []
quickSort (h:tl) | tl == [] = [h]
                 | otherwise = [x | x <- quickSort tl, x <= h]
                               ++ [h] ++ [y | y <- quickSort tl, y > h]