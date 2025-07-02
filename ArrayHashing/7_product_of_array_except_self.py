"""
Problem: Product of Array Except Self
LeetCode: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that
answer[i] is equal to the product of all the elements of nums except nums[i].

You must solve it without using division and in O(n) time.

-----------------------------------------------------------
🔍 Logic:
- Use two arrays:
  1. prefix: prefix[i] = product of all elements before index i
  2. suffix: suffix[i] = product of all elements after index i
- Multiply prefix[i] and suffix[i] to get the product of all elements except nums[i].

Example:
nums = [1, 2, 3, 4]
prefix = [1, 1, 2, 6]  # products before each index
suffix = [24, 12, 4, 1] # products after each index
result = [24, 12, 8, 6]  # element-wise multiplication

-----------------------------------------------------------
Time Complexity: O(n)
- We traverse the input array a constant number of times.
- Each pass is O(n), so total time is O(n).

Space Complexity: O(n)
- We use three arrays of size n: prefix, suffix, and result.
- Extra space is O(n).
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        res = [0] * n

        # Build prefix products
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Build suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        # Construct result by multiplying prefix and suffix products
        for i in range(n):
            res[i] = prefix[i] * suffix[i]
        
        return res
