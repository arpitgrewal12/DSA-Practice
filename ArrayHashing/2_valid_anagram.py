"""
Problem: Valid Anagram
LeetCode: https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

from typing import Dict
from collections import defaultdict

# -----------------------------------------------------------
# 📘 Approach 1: Using Regular Dictionary
# Count characters in both strings and compare maps
# Time: O(n), Space: O(1) – Since only lowercase letters are involved
# -----------------------------------------------------------

class SolutionDict:
    def isAnagram(self, s: str, t: str) -> bool:
        myMapS =  {}
        myMapT = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            myMapS[s[i]] = 1 + myMapS.get(s[i], 0)
            myMapT[t[i]] = 1 + myMapT.get(t[i], 0)

        return myMapS == myMapT


# -----------------------------------------------------------
# 📘 Approach 2: Using defaultdict
# Simplifies logic by eliminating need for get()
# Time: O(n), Space: O(1)
# -----------------------------------------------------------

class SolutionDefaultDict:
    def isAnagram(self, s: str, t: str) -> bool:
        myMapS = defaultdict(int)
        myMapT = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            myMapS[s[i]] += 1
            myMapT[t[i]] += 1

        return myMapS == myMapT


# -----------------------------------------------------------
# 🔍 Hint:
# When using defaultdict(int), you don’t need to use .get() because
# missing keys default to 0. Just use myMap[key] += 1 to count.
# -----------------------------------------------------------
