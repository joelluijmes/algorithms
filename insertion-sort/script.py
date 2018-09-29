def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    return arr


arr = [9, 5, 3, 8, 7, 2, 1, 0, 4, 6]
res = list(range(10))

print(insertion_sort(arr))
