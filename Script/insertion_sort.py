arr = [4, 2, 7, 1, 3]
q = len(arr)


def insertion_sort(arr):
    for j in range(1, q):
        i = arr[j]
        j = j - 1
        while j >= 0 and i < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = i


serek = insertion_sort(arr)
print(arr)
