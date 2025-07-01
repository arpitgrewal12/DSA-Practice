"""
Problem: Two Sum
LeetCode: https://leetcode.com/problems/two-sum/

Given an array of integers `nums` and an integer `target`, return the indices of the 
two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

Return the answer in any order.
"""

from typing import List

# -----------------------------------------------------------
# 📘 Approach: Hash Map (value → index)
# Traverse the array while storing value → index in a dictionary.
# For each number, compute the complement (target - val)
# If the complement is already in the map, return its index and current index.
# Time: O(n): One pass over the array; constant-time work per item,
# Space: O(n): Hash map stores up to n elements (value → index)
# -----------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        myMap = {}  # val → index
        res = []

        for i, val in enumerate(nums):
            complement = target - val
            if complement in myMap:
                res.append(myMap[complement])  # index of complement
                res.append(i)                  # current index
                break                          # return only one valid pair
            myMap[val] = i  # store current value with its index

        return res
