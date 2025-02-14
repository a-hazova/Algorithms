def devide(unsorted, start, end):
    if end <= start:
        return
    mid = (start + end) // 2

    devide(unsorted, start, mid)
    devide(unsorted, mid+1, end)

    merge(unsorted, start, mid, mid+1, end)

def merge(unsorted, l_start, l_end, r_start, r_end):
    i, j = l_start, r_start

    sorted = []

    while i <= l_end and j <= r_end:
        if unsorted[i] < unsorted[j]:
            sorted.append(unsorted[i])
            i += 1
        else: 
            sorted.append(unsorted[j])
            j += 1
    
    if i <= l_end:
        sorted + unsorted[i : l_end]
    if j <= r_end:
        sorted + unsorted[j : r_end]
    
    for k, i in enumerate(range(l_start, r_end + 1)):
        unsorted[k] = sorted[i]

arr = [8, 5, 7, 1, 4, 6]

devide(arr, 0, len(arr))

