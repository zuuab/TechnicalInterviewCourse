# reverse the value and the key

def reverseMe(dict):
    newDict = {}

    for k, v in dict.items():
        tempK = v
        tempV = k

        newDict[tempK] = tempV

    return newDict


test_dict = {'B': 4, 'Y': 2, 'U': 5}

print(reverseMe(test_dict))
