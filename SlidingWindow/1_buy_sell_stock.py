"""
Problem: Best Time to Buy and Sell Stock
LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array `prices` where prices[i] is the price of a given stock on the i-th day.
You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell it.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

-----------------------------------------------------------
💡 Approach: Two Pointers (Sliding Window)

- Use two pointers: 
  - `l` for the **buy day**
  - `r` for the **sell day**
- If `prices[r] > prices[l]`, it’s a **profitable** transaction.
  → compute the profit and update maxProfit.
- If `prices[r] <= prices[l]`, it's **not profitable** to sell at `r`.
  → move `l = r`, because we found a **lower buying price**.
- Always move `r += 1` to continue checking future days.

📌 Why not use `l += 1`?
- Because we're not just incrementing blindly.
- If the current `r` gives a lower price, it's better to buy at `r` instead of keeping `l`.

-----------------------------------------------------------
🕒 Time Complexity: O(n)
- Traverse the prices list once with two pointers.

🧠 Space Complexity: O(1)
- Constant space used for pointers and profit variables.
-----------------------------------------------------------
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # buy pointer
        r = 1  # sell pointer
        maxProfit = 0
        profit = 0

        while r < len(prices):
            # profitable transaction?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                # lower price found — better buying day
                l = r
            r += 1

        return maxProfit
