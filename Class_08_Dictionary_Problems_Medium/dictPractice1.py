# example problem 1
# convert a list of tuplels into a dictionary


tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]


def convertTup(list):
    myDict = {}
    myDict = dict(list)
    return myDict


print(convertTup(tups))
