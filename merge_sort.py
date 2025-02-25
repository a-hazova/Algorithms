def devide(arr, start =  0, end = None):
    if end is None:
        end = len(arr)-1

    if  end - start <= 1:
        return
    mid = (start + end) // 2

    devide(arr, start, mid)
    devide(arr, mid, end)

    merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left = arr[start: mid]
    right = arr[mid: end]
    i = start
    l, r = 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            arr[i] = left[l]
            l += 1
        else: 
            arr[i] = right[r]
            r += 1
        i += 1
    while l < len(left):
        arr[i] = left[l]
        l += 1
        i += 1
    while r < len(right):
        arr[i] = right[r]
        r += 1
        i += 1
arr = [8, 5, 7, 1, 4, 6]

devide(arr)

print(arr)  # Output: [1, 4, 5, 6, 7, 8]


