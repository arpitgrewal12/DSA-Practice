# Problem: Find Minimum in Rotated Sorted Array  
# LeetCode: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Suppose an array of length `n` sorted in ascending order is rotated between 1 and n times.  
# You are given the rotated array `nums` with **no duplicate values**, and you must return the **minimum element**.

# You must write an algorithm that runs in **O(log n)** time.

from typing import List

# -----------------------------------------------------------
# 📘 Approach: Binary Search
# - Use binary search to locate the pivot (minimum) element.
# - The array is split into two sorted parts due to rotation.
# - If mid element >= left, then left portion is sorted,
#   so minimum lies in the right portion → shift left pointer.
# - Else, minimum lies in the left portion → shift right pointer.
# - Also check if entire segment is sorted (nums[l] < nums[r]).
# - Track the minimum during each iteration.

# - The rotated array is composed of two sorted portions.
# - Example: [3, 4, 5, 1, 2]
#   - mid = 5 → potential result
#   - right sorted portion [1, 2] contains smaller values
# - Example 2: [5, 1, 2, 3, 4]
# - mid = 1 → nums[mid] < nums[l] (1 < 5)
#   → left portion [5, 1] is **not** sorted → minimum must be in left portion
#   → move r = mid - 1 to search in left half

# 🔍 Key Idea:
# - If nums[mid] >= nums[l], then the left portion [l..mid] is sorted.
#   → That means minimum must be in the **right half**, so shift left.
# - Else, the right portion is unsorted → minimum is in the **left half**, so shift right.
# - We use >= instead of > because mid can equal l when checking.
#
# 📎 Edge Case:
# - If current subarray [l..r] is sorted (nums[l] < nums[r]), 
#   then nums[l] is the minimum in that portion. Early exit.
#
# ✅ Track minimum value during each iteration with res = min(res, nums[mid])
#
# Time: O(log n) — Binary search halves the search space each time.
# Space: O(1) — Only constant space used for pointers and result.
# -----------------------------------------------------------

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]  # Start with the first element as candidate

        while l <= r:
            # If subarray is sorted, take leftmost as minimum
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])

            # Left half is sorted — pivot must be in right half
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                # Pivot is in left half
                r = mid - 1

        return res
