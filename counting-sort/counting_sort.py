def counting_sort(items):
    if len(items) == 0 or len(items) == 1: return items

    min_value = items[0]
    max_value = items[0]

    for item in items:
        if item < min_value:
            min_value = item
        elif item > max_value:
            max_value = item

    diff = max_value - min_value + 1

    counts = [0 for _ in range(diff)]
    output = [0 for _ in range(diff)]

    for item in items:
        counts[item - min_value] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    for item in items:
        output[counts[item - min_value] - 1] = item
        counts[item - min_value] -= 1
    
    return output[:len(items)]


if __name__ == '__main__':
    items = [-2, -23, 8, 5, 1, 6, 12, 7, 3, 0, 2]

    items = counting_sort(items)

    print (items)
