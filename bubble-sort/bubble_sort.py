#Implementation of bubble sort in python.

def bubble_sorted(items):
    """creates a new list, sorts it using bubble_sort,
    then returns the new sorted list. The original list
    is left untouched."""
    from copy import deepcopy

    new = deepcopy(items)
    bubble_sort(new) #new is modified
    return new
    
def bubble_sort(items):
    """sorts the given list in place"""
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                is_sorted = False
    return items #items is modified

if __name__ == "__main__":
    #executes this piece of code if the user runs this script directly,
    #i.e. not by importing.

    print("enter a space seperated list of numbers like 5 4 73 1.")
    item_list = bubble_sort(list(map(int, input("integers to be sorted: ").split())))

    #print(*[1,2,3]) is equivalent to print(1, 2, 3)
    print(*item_list)
