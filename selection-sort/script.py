def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        smallest = i

        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j

        arr[i], arr[smallest] = arr[smallest], arr[i]

    return arr


arr = [9, 5, 3, 8, 7, 2, 1, 0, 4, 6]
res = list(range(10))

assert selection_sort(arr) == res
