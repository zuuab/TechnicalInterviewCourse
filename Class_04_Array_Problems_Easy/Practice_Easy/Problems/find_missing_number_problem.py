# Write a function that finds the missing number in an array

input_array = [1, 2, 3, 4, 6, 7]
# Output = 5


def find_missing(array):
    for i in range(len(array) - 1):
        if ((array[i + 1]) - array[i]) > 1:
            return array[i] + 1


print(find_missing(input_array))
