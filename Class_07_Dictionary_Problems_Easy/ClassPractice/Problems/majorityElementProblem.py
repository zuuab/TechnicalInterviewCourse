# /*
# Given an array nums of size n, return the majority element.
# The majority element is an element that appears more than [n/2] times.
# You may assume that the majority element always exists in the array.

# Input = [3, 2, 3]
# Output = 3

# Input = [2, 2, 1, 1, 1, 2, 2]
# Output = 2

# Source: https://leetcode.com/problems/majority-element/
# */

arr1 = [3, 2, 3]  # 3
arr2 = [2, 2, 1, 1, 1, 2, 2]  # 2


def majority(array):
    mid = len(array) // 2

    dictCount = {}

    for i in range(0, len(array)):
        if array[i] in dictCount:
            dictCount[array[i]] = dictCount[array[i]] + 1
        else:
            dictCount[array[i]] = 1

    for k, v in dictCount.items():
        if v >= mid:
            return k


print(majority(arr1))
print(majority(arr2))
