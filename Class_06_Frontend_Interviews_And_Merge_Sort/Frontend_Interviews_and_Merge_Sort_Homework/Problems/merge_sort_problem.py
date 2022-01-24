# Write a merge sort algorithm to sort an array.
# The function should return the sorted array.

# two examples
# output: [3, 9, 15, 24, 45, 50, 77, 98]
from pandas import array


array1 = [45, 98, 3, 24, 15, 77, 9, 50]
array2 = [18, 16, 27, 4, 12]  # output: [4, 12, 16, 18, 27]


def MergeSortMain(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        MergeSortMain(left)
        MergeSortMain(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


MergeSortMain(array2)
print(array2)
