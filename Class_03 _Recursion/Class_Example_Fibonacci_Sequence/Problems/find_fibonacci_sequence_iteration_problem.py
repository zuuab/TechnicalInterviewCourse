# Write a program that creates a portion of the fibonacci sequence iteratively


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        fn = 0
        fn1 = 1
        fn2 = 2
        for i in range(3, n):
            fn = fn1 + fn2
        return fn


n = input(
    "Choose a position in the fibonacci sequence, I'll tell you the corrisponding value: ")
print(fib(n))
