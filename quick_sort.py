
random_list_of_nums = [22, 5, 1, 77, 8, 91, 18, 99]


def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list)//2]
    left = [item for item in list if item < pivot]
    right = [item for item in list if item > pivot]
    middle = [item for item in list if item == pivot]

    return quick_sort(left) + middle + quick_sort(right)

# print(quick_sort(random_list_of_nums))


def quick_sort2(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    if start >= end:
        return
    pivot = nums[(start + end)//2]
    i, j = start, end
    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1

        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1

    quick_sort2(nums, start, j)
    quick_sort2(nums, i, end)


quick_sort2(random_list_of_nums)
print(random_list_of_nums)
