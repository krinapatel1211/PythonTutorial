

array = [2, 8, 5, 3, 9, 4, 1]

for item in range(len(array)):
    for j in range(0, (len(array) - item - 1)):
        if array[j] > array[j + 1]:
            (array[j], array[j + 1]) = (array[j + 1], array[j])

for k in array:
    print(k, end="")
