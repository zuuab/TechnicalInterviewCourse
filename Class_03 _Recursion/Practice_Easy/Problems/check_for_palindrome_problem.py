# Write a function that checks if a string is a palindrome using recursion

def pal(n):
    if len(n) <= 1:
        return True
    if n[0] == n[len(n) - 1]:
        return pal(n[1:-1])
    return False


print(pal("racecar"))
print(pal("aaron"))
print(pal("Ilovepalindromes"))
print(pal("IlovepalindromessemordnilapevolI"))
