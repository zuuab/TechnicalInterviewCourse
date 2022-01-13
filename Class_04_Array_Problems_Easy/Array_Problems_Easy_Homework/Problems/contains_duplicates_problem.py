# Given an array of integers, find if the array contains any duplicates
# Your function should return false if every element is distinct.
# This problem came from leetcode.com

from typing import Any


input_array = [1, 2, 3, 3, 4]
# Output = True


# initial solution, double for loop
def AnyRepeats(val):
    for i in range(0, len(val)):
        for j in range((i+1), len(val)):
            if val[i] == val[j]:
                return True
    return False


print(AnyRepeats(input_array))


# optimized solution, single for loop
def AnyRepeatsOptimized(val):
    testSet = []
    for i in range(0, len(val)):
        if val[i] in testSet:
            return True
        testSet.append(val[i])
    return False


print(AnyRepeatsOptimized(input_array))
