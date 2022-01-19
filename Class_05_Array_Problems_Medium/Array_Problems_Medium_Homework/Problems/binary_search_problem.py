# Search an array of numbers to find a target number using binary search.
# The function should return the index of the target number if the target number is found
# or a -1 if the target is not found in the array.

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


input_array = [1, 2, 5, 9, 12, 15, 21, 28, 99, 100, 117]
input_target = 5
# Output = 2

print(BinarySearch(input_array, input_target))
