# /**

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

# A sentence is a string of single-space separated words where each word consists only of lowercase letters.
# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Input: s1 = “this apple is sweet”, s2 = “this apple is sour”
# Output: [“sweet”, “sour”]

# Input: s1 = “apple apple”, s2 = “banana”
# Output: [“banana”]

# Source: https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Solution walkthrough: https://medium.com/nerd-for-tech/problem-solving-patterns-frequency-counter-20205a1ecfb7
# */

from enum import unique


s1 = 'this apple is sweet'
s2 = 'this apple is sour'

s3 = 'apple apple'
s4 = 'banana'


def split(str1, str2):
    words = str1.split()
    words.extend(str2.split())
    unique = {}

    for word in words:
        if word not in unique:
            unique[word] = 1
        else:
            unique.pop(word)

    return list(unique.keys())


print(split(s1, s2))
print(split(s3, s4))
