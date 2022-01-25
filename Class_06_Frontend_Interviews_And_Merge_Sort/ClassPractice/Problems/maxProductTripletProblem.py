
# Examples:
# Input = [10, 3, 5, 6, 20]
# Output = 1200 (product of 10, 6, and 20)

# Input:  [-10, -3, -5, -6, -20]
# Output: -90

# Input:  [1, -4, 3, -6, 7, 0]
# Output: 168


factors1 = [10, 3, 5, 6, 20]  # 1200
factors2 = [-10, -3, -5, -6, -20]  # -90
factors3 = [1, -4, 3, -6, 7, 0]  # 168


def Sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[mid:]
        right = arr[:mid]

        Sort(left)
        Sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def Max(arr):
    if len(arr) > 2:
        length = len(arr) - 1
        topMax = arr[length] * arr[length - 1] * arr[length - 2]
        bottomMax = arr[0] * arr[1] * arr[length]
    if topMax >= bottomMax:
        return topMax
    else:
        return bottomMax


Sort(factors1)
Sort(factors2)
Sort(factors3)

print(Max(factors1))
print(Max(factors2))
print(Max(factors3))
