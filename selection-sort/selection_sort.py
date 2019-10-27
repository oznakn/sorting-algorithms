def selection_sort(arr):
    tempL=[]
    arrlen=len(arr)
    for i in arr:
        tempL.append(i)

    for i in range(arrlen):
        mnindex = i

        for j in range(i + 1, len(arr)):
            if tempL[j] < tempL[mnindex]:
                mnindex = j

        tempL[mnindex], tempL[i] = tempL[i], tempL[mnindex]

    return tempL

def selection_inplace(arr):
    for i in range(len(arr)):
        mn = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mn]:
                mn = j

        arr[mn], arr[i] = arr[i], arr[mn]

    return arr

L=[-2, 10, -3, 5, 12, 0, 15]
a = selection_sort(L)
print("a:",a)
print("L:",L)
selection_inplace(L)
print("L:",L)
