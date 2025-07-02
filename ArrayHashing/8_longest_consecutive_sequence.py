"""
Problem: Longest Consecutive Sequence
LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

-----------------------------------------------------------
🔍 Logic:
- Convert the list to a set for O(1) lookups.
- For each number, check if it's the start of a sequence (i.e., num - 1 not in set).
- If it is, count consecutive numbers (num, num+1, num+2, ...) in the set.
- Track and update the maximum length found.

Example:
nums = [100, 4, 200, 1, 3, 2]
Longest consecutive sequence is [1, 2, 3, 4], length = 4

-----------------------------------------------------------
Time Complexity: O(n)
- Each number is visited at most twice: once in the initial loop,
  and once while counting consecutive numbers.
- Set lookups are O(1) on average.

Space Complexity: O(n)
- Extra space for the set storing all numbers.
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        mySet = set(nums)  # O(n) space for set

        for num in nums:
            # Only start counting if num is the start of a sequence
            if num - 1 not in mySet:
                curr_len = 1
                # Count consecutive numbers after current num
                while num + curr_len in mySet:
                    curr_len += 1
                
                max_len = max(max_len, curr_len)
        
        return max_len
