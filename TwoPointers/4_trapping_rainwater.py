"""
Problem: Trapping Rain Water
LeetCode: https://leetcode.com/problems/trapping-rain-water/

Given `height`, an array representing elevation at each index, return the total amount of water that can be trapped after raining.

-----------------------------------------------------------
🧠 Approach: Two-Pointer Technique

- Use two pointers (`l` and `r`) starting from both ends.
- Keep track of the max height seen so far from both sides (`maxL`, `maxR`).
- At every step:
    - If `maxL < maxR`, water trapped at `l` depends on `maxL`.
        → Water = `maxL - height[l]` if `maxL > height[l]`
        → Then move `l` forward.
    - Else, water trapped at `r` depends on `maxR`.
        → Water = `maxR - height[r]`
        → Then move `r` backward.
- This works because water trapped at any point depends on the **shorter boundary**.

-----------------------------------------------------------
Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation:
Water is trapped between bars — we accumulate the difference between current height and the min boundary so far.

-----------------------------------------------------------
🕒 Time Complexity: O(n)
- Each element is visited at most once by either pointer.

🧠 Space Complexity: O(1)
- Only constant extra variables used (`l`, `r`, `maxL`, `maxR`, `area`).
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        area = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                area += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                area += maxR - height[r]

        return area
