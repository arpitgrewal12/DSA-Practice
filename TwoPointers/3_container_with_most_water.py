"""
Problem: Container With Most Water
LeetCode: https://leetcode.com/problems/container-with-most-water/

You are given an integer array `height` of length n.
There are n vertical lines drawn such that the two endpoints of the i-th line are at (i, 0) and (i, height[i]).
Find two lines that, together with the x-axis, form a container that holds the most water.

-----------------------------------------------------------
🧠 Approach: Two Pointer Technique

- Initialize two pointers: one at the beginning (`l`), one at the end (`r`) of the list.
- At each step, calculate the area formed between the two lines:
  area = min(height[l], height[r]) * (r - l)

- Move the pointer that points to the **shorter line**, because:
  - A taller line *might* give a bigger area, but the current shorter line is the limiting factor.
  - Reducing width (by moving the taller line) won't help unless height increases.

-----------------------------------------------------------
🕒 Time Complexity: O(n)
- Each element is visited at most once by `l` or `r`.

🧠 Space Complexity: O(1)
- Uses only constant extra space.
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxArea = 0

        while l < r:
            # Calculate current area using shorter of the two heights
            area = min(heights[l], heights[r]) * (r - l)
            maxArea = max(maxArea, area)

            # Move the pointer pointing to the shorter height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
