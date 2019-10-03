items = [1, 5, 13, 36, 2, 1000, 23]

is_sorted = False

while not is_sorted:
    is_sorted = True

    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            items[i], items[i + 1] = items[i + 1], items[i]
            is_sorted = False

print(items)

