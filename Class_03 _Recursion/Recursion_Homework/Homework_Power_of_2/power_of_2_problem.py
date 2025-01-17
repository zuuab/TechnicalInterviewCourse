# Given an integer n, return True if it is a power of 2.
# An integer n is a power of two, if there exists an integer x such that n == 2^x

# Examples:

# Input: n = 4
# Output: True
# 2^2 = 4

# Input : n = 16
# Output : True
# 2^4 = 16

# Input : n = 13
# Output : False

# example input/output
# 0 -- 1
# 1 -- 2
# 2 -- 4
# 3 -- 8
# 4 -- 16
# 5 -- 32

def power(n):
    if n == 1 or n == 2:
        print('True')
        return True
    elif n < 2:
        print("false")
        return False
    else:
        return power(n / 2)


n = int(input("Input a number: "))
power(n)
