# merge sort implemented in python3

def merge_sort(lst):
    """
    Calls the helper function to sort the given list.
    The helper function uses the divide and conquer technique
    to sort sub-lists and uses the merge() function to merge the
    sorted lists.
    """
    

    def merge(lst1, lst2):
        new = []
        #in this step merge the two lists by checking their 0'th index
        #until one of the lists is exhausted.
        while lst1 and lst2:
            #compare the smallest element of the both lists and move that
            #element to the new list.
            if lst1[0] < lst2[0]:
                new.append(lst1.pop(0))
            else:
                new.append(lst2.pop(0))

        #append the existing list to the new list.
        if lst1:
            new.extend(lst1)
        elif lst2:
            new.extend(lst2)

        return new

    def ms_helper(lst, left, right):
        #return the list if the sub list is a single element, i.e. sorted.
        if right == left:
            return [lst[right]]
        middle = (left + right) // 2
        #divide and conquer.
        return merge(ms_helper(lst, left, middle), ms_helper(lst, middle+1, right))

    return ms_helper(lst, 0, len(lst)-1)


if __name__=="__main__":
    print("enter a space seperated list of numbers like 5 4 73 1.")
    original_list = list(map(int, input("integers to be sorted: ").split()))
    sorted_list = merge_sort(original_list)

    #print(*[1,2,3]) is equivalent to print(1, 2, 3)
    print(*sorted_list)
