# Write a function that reverses an array

input_array = [1, 2, 3, 4, 5, 6, 7, "a"]
# Output = ["a", 7, 6, 5, 4, 3, 2, 1]


def reverse_array(var):
    newArray = []
    for i in range((len(var) - 1), -1, -1):
        newArray.append(var[i])
    return newArray


print(reverse_array(input_array))


def reverse(array):
    if len(array) <= 1:
        return array
    for i in len(array):
        array[0] == array[len(array) - 1]
        return array(array[1:-1])
