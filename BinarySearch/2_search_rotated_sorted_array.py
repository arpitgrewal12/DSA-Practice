# Problem: Search in Rotated Sorted Array  
# LeetCode: https://leetcode.com/problems/search-in-rotated-sorted-array/

# You are given an integer array `nums` sorted in ascending order (with distinct values), 
# and an integer `target`.

# `nums` was rotated at an unknown pivot and you must search for `target`.  
# If found, return its index; otherwise, return -1.

# You must write an algorithm with **O(log n)** runtime complexity.
from typing import List

# -----------------------------------------------------------
# 📘 Approach: Modified Binary Search
# - At each step, determine which half of the array is sorted.
# - Then decide if the target lies within the sorted half.
# - If yes, continue search in that half; otherwise, search the other.
#
# 🧠 Example: [4, 5, 6, 7, 0, 1, 2], target = 0
# - mid = 7 → mid is in left sorted portion.
# - Since 0 < 7 and 0 > 4 is false, target must be in right portion → shift left = mid + 1
#
# ✅ Steps:
# - Check if nums[mid] == target → return mid
# - If nums[mid] >= nums[l]: left portion is sorted
#   - If target in [nums[l], nums[mid]] → search left
#   - Else → search right
# - Else: right portion is sorted
#   - If target in [nums[mid], nums[r]] → search right
#   - Else → search left
#
# Time: O(log n)
# Space: O(1)
# -----------------------------------------------------------

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # Search left half
                else:
                    l = mid + 1  # Search right half

            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # Search right half
                else:
                    r = mid - 1  # Search left half

        return -1
