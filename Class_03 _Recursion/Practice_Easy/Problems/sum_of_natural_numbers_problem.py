# Write a function that sums all natural numbers that lead up to a given value using recursion

def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n - 1) + n


print(sum(4))
