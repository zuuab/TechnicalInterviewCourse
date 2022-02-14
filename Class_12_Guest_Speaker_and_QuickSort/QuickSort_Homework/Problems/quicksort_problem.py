def quickSort(nums):
    length = len(nums)
    if length <= 1:
        return nums
    else:
        pivot = nums.pop()

    greater = []
    less = []

    for item in nums:
        if item > pivot:
            greater.append(item)
        else:
            less.append(item)
    return quickSort(less) + [pivot] + quickSort(greater)


testNums = [0, 1, 5, 6, 9, 7, 1, 2, 5, 5, 9, 0]

print(quickSort(testNums))
