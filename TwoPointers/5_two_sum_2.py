"""
Problem: Two Sum II - Input Array Is Sorted
LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

You are given a 1-indexed array of integers `numbers` that is sorted in non-decreasing order.
You need to find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-based).

-----------------------------------------------------------
🧠 Approach: Two Pointers

- Since the array is sorted, use two pointers: one at the beginning and one at the end.
- If the sum is greater than target, move the right pointer leftward.
- If the sum is less than target, move the left pointer rightward.
- If equal, return the 1-based indices.

-----------------------------------------------------------
Example:
numbers = [2, 7, 11, 15], target = 9

Start:
  l = 0 → 2
  r = 1 → 7

Sum = 2 + 7 = 9 → ✅ return [1, 2]

-----------------------------------------------------------
🕒 Time Complexity: O(n)
- Single pass with two pointers from both ends.

🧠 Space Complexity: O(1)
- Only using variables, no extra data structures.
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            sums = numbers[l] + numbers[r]

            if sums == target:
                return [l + 1, r + 1]  # 1-indexed result
            elif sums > target:
                r -= 1
            else:
                l += 1

        return []  # If no valid pair found (though per problem, exactly one solution exists)
