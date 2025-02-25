def shell_sort(arr):
    n = len(arr)
    step = n // 2
    while step > 0:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while  j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp
        step //= 2
    return arr

arr = [12, 11, 13, 5, 6, 7, 8, -3]
print("Sorted array is:", shell_sort(arr))