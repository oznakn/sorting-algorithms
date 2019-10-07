import math


def bucket_sort(input_array):
    bucket = list()
    sorted_array = list()
    slots = 10

    for i in range(slots):
        bucket.append(list())
    div = math.ceil((max(input_array)+1)/10)

    for i in input_array:
        element = i//div
        bucket[element].append(i)

    for i in range(slots):
        bucket[i] = sorted(bucket[i])  

    for i in range(slots):
        for j in range(len(bucket[i])):
            sorted_array.append(bucket[i][j])
    return sorted_array


if __name__ == '__main__':
    user_input = int(input("Enter number of elements in your array: "))
    input_array = list(map(int, input("\nEnter the array elements separated by spaces: ").strip().split()))[:user_input]
    sorted_array = bucket_sort(input_array)
    print('Here is your sorted array: ' + ','.join(str(number) for number in sorted_array))
