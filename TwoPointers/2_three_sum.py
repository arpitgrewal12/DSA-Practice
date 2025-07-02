"""
Problem: 3Sum
LeetCode: https://leetcode.com/problems/3sum/

Given an integer array `nums`, return all the unique triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

-----------------------------------------------------------
🧠 Approach:
- Sort the array to efficiently skip duplicates and use two-pointer technique.
- Fix one element at a time (index `i`), then use two pointers (`l`, `r`) to find two other numbers that sum to `-nums[i]`.
- Skip duplicate values to avoid repeated triplets.

-----------------------------------------------------------
Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Sorted:         [-4, -1, -1, 0, 1, 2]
Output:         [[-1, -1, 2], [-1, 0, 1]]

-----------------------------------------------------------
Time Complexity: O(n^2)
- Outer loop runs O(n) times, inner two-pointer scan is O(n) → total O(n^2)

Space Complexity: O(1) (excluding output)
- No extra space used apart from the result list.
- If you consider the result list, space is O(k) where k = number of triplets

-----------------------------------------------------------
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array to make it easier to skip duplicates
        res = []

        for i in range(len(nums)):
            # Skip duplicate values for the first element in the triplet
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer setup
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # Move left pointer and skip duplicates
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    # No need to move `r` here since `l < r` covers the full range

                elif total < 0:
                    # Sum too small, move left to increase it
                    l += 1
                else:
                    # Sum too big, move right to decrease it
                    r -= 1

        return res
