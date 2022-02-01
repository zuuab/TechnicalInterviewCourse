# remove duplicate values across dictionaries


def uniqueValues(dict):
    myList = []
    numsList = []
    for k, v in dict.items():
        myList.append(dict[k])
    for k in myList:
        for v in myList
        numsList.append(myList[k][v])

    print(numsList)
    return myList


test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}

print(uniqueValues(test_dict))
