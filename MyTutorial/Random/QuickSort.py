def quickSort(arr, left, right):
    if left < right:
        pi = partition(arr, left, right)
        quickSort(arr, left, pi - 1)
        quickSort(arr, pi + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    print("Pivot = ", pivot)
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
            print("i = ", i, "arr[i] = ", arr[i])
        while j > left and arr[j] >= pivot:
            j -= 1
            print("j = ", j, "arr[j] = ", arr[j])
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
        print(arr)
    return i


# elements = [6, 5, 8, 3, 5, 1, 0, 3]
elements = [40, 21, 8, 17, 51, 34]
quickSort(elements, 0, len(elements) - 1)
