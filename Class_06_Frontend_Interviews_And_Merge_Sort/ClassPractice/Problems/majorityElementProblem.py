
from platform import java_ver


arr1 = [3, 2, 3]  # 3
arr2 = [2, 2, 1, 1, 1, 2, 2]  # 2


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


def FindMid(array):
    mid = len(array) // 2
    return array[mid]


MergeSortMain(arr1)
print(arr1)
print(FindMid(arr1))

MergeSortMain(arr2)
print(arr2)
print(FindMid(arr2))
