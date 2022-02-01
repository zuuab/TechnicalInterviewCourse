# practice 3
# sort nested keys by value

def sortThis(dict):
    newDict = sorted(dict.items(), key=lambda x: x[1]['marks'])

    return newDict


test_dict = {'Nikhil': {'roll': 24, 'marks': 17},
             'Akshat': {'roll': 54, 'marks': 12},
             'Akash': {'roll': 12, 'marks': 15}}

print(sortThis(test_dict))
