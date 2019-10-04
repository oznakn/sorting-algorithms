def selection_sort(arr):
    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[min], arr[i] = arr[i], arr[min]

    return arr


a = selection_sort([-2, 10, -3, 5, 12, 0, 15])
print(a)
