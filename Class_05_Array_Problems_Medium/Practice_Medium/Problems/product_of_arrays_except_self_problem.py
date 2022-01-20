# Given an array nums of n integers where n > 1, return an array output such that output[i]
# is equal to the product of all the elements of nums except nums[i]
# Note: Please solve it without division
# This problem came from leetcode.com

def LetsDoThis(array):
    new_array = []
    for i in range(0, len(array)):
        tempVal = 1
        for j in range(0, len(array)):
            if j != i:
                tempVal = array[j] * tempVal
        new_array.append(tempVal)
    return new_array


input_array = [1, 2, 3, 4]
# Output = [24, 12, 8, 6]

print(LetsDoThis(input_array))
