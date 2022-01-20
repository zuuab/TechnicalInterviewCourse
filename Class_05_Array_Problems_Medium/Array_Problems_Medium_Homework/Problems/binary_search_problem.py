# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

from tkinter.font import families


def BinarySearch(array, n):
    l = 0
    u = len(array)-1
    while l <= u:
        mid = (l+u) // 2

        if array[mid] == n:
            return mid
        elif array[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return -1


input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
# Output = 2

print(BinarySearch(input_array, input_target))


def Search(array, n):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (high+low) // 2
        if array[mid] == n:
            return mid
        elif array[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return -1


input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 7
# Output = 2


print(Search(input_array, input_target))


def OtherType(array):
    low = 0
    high = len(array)-1

    while low < high:
        mid = (high+low) // 2
        if array[mid] > array[high]:
            low = mid + 1
        else:
            high = mid
    return array[low]


new_array = [3, 4, 5, 6, 1, 2]

print(OtherType(new_array))


def MaxPivot(array):
    low = 0
    high = len(array) - 1
    while low < high:
        mid = (high+low) // 2
        if array[mid] < array[low]:
            high = mid - 1
        else:
            low = mid
    return array[high]


print(MaxPivot(new_array))
