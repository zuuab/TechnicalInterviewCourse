# /**
#  * Given two strings s and t, return true if t is an anagram of s, and false otherwise. Use a dictionary.
#  *
#  * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  * typically using all the original letters exactly once.
#  *
#  * Input: s = "anagram", t = "nagaram"
#  * Output: true
#  *
#  * Input: s = "rat", t = "car"
#  * Output: false
#  *
#  * Source: https://leetcode.com/problems/valid-anagram/
#  */
from collections import defaultdict

s = 'anagram'
t = 'nagaram'


def isAnagram(s, t) -> bool:

    if len(s) != len(t):
        return False

    hash_s = defaultdict(int)
    hash_t = defaultdict(int)

    for i in range(len(s)):
        hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
        hash_t[t[i]] = 1 + hash_t.get(t[i], 0)

    for key in hash_s:
        if key not in hash_t:
            return False

        else:
            if hash_t[key] != hash_s[key]:
                return False

    return True


print(isAnagram(s, t))
