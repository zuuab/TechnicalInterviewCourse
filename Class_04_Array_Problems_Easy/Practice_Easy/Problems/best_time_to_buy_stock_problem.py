# Say you have an array for which the ith element is the price of a given stock on day i
# If you were only permitted to complete at most one transaction (i.e, buy one and
# sell one share of the stock) design an algorithm to find the maximum profit
# This problem came from leetcode.com

input_array = [7, 1, 5, 3, 6, 4]
# Output = 5
# i = price


# initial solution, double for loop
def MaxProfit(val):
    max = 0
    for i in range(0, len(val)):
        for j in range((i + 1), len(val)):
            if (val[j] - val[i]) > max:
                max = val[j] - val[i]
    return max


print(MaxProfit(input_array))


# optimized solution, single for loop
def MaxProfitOptimized(val):
    max = 0
    min = val[0]

    for i in range(0, len(val)):
        if val[i] < min:
            min = val[i]
        if (val[i] - min) > max:
            max = (val[i] - min)
    return max


print(MaxProfitOptimized(input_array))
