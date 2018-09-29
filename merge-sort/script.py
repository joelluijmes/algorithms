def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr

    h = n // 2
    left = merge_sort(arr[0:h])
    right = merge_sort(arr[h:])

    indexLeft = 0
    indexRight = 0
    for index in range(n):
        if indexLeft >= len(left):
            arr[index] = right[indexRight]
            indexRight += 1
        elif indexRight >= len(right):
            arr[index] = left[indexLeft]
            indexLeft += 1
        elif left[indexLeft] <= right[indexRight]:
            arr[index] = left[indexLeft]
            indexLeft += 1
        else:
            arr[index] = right[indexRight]
            indexRight += 1

    return arr


arr = [9, 5, 3, 8, 7, 2, 1, 0, 4, 6]
res = list(range(10))

assert merge_sort(arr) == res
