def binary_search(arr, value):
    def loop(x, y):
        if x < y:
            h = (x + y) // 2
            return loop(h + 1, y) if arr[h] < value else loop(x, h)

        return x if arr[x] == value else None

    return loop(0, len(arr) - 1)


arr = list(range(10))

assert binary_search(arr, 10) == None
assert binary_search(arr, -1) == None
assert binary_search(arr, 5) == 5
assert binary_search(arr, 9) == 9
