# Write a function that moves all negative elements to the end of an array

input_array = [-1, 2, -3, 4, 5, 7]
# Output = [2, 4, 5, 7, -3, -1]


def NegEnd(array):
    negs = []
    for i in range(len(array) - 2):
        if array[i] < 0:
            negs.append(array.pop(i))
    for i in range(len(negs)):
        array.append(negs[i])
    return array


print(NegEnd(input_array))
