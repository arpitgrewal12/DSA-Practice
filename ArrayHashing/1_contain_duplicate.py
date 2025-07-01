"""
Problem: Contains Duplicate
LeetCode: https://leetcode.com/problems/contains-duplicate/

Given an integer array `nums`, return `true` if any value appears at least twice 
in the array, and return `false` if every element is distinct.
"""

from typing import List

# -----------------------------------------------------------
# 📘 Approach 1: Hash Set
# Add each number to a set and check for duplicates
# Time: O(n), Space: O(n)
# -----------------------------------------------------------

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# -----------------------------------------------------------
# 🔍 Hint:
# In Python, `set.add()` always returns `None`, so using it in a conditional like
# `if not mySet.add(num):` won't work.
# Instead, check `if num in mySet` before calling `.add(num)`.
# -----------------------------------------------------------