"""
Problem: Longest Repeating Character Replacement
LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string `s` and an integer `k`. You can replace at most `k` characters 
in the string so that all characters in the window are the same.
Return the length of the longest such valid substring.
"""

from collections import defaultdict

"""
Problem: Longest Repeating Character Replacement
LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string `s` and an integer `k`.
You can replace at most `k` characters in the string so that all characters in the window are the same.
Return the length of the longest such valid substring.
"""

# -----------------------------------------------------------
# 📘 Approach: Sliding Window with Inner Shrink (No maxFreq variable)
# - Maintain a frequency map of characters inside the current window.
# - Keep expanding the right side.
# - Shrink the window from the left if more than k replacements are needed.
#
# Key condition:
#     (window size) - (most frequent character count) > k
#   If this is True, we shrink from the left.
#
# Time: O(26 * n) → O(n), since max 26 characters
# Space: O(1) → only 26 letters stored in map
# -----------------------------------------------------------

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freqMap = {}

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)

            # Shrink the window if too many replacements would be needed
            while (r - l + 1) - max(freqMap.values()) > k:
                freqMap[s[l]] -= 1
                l += 1  # shrink left

            # Always update result as max valid window seen so far
            res = max(res, r - l + 1)

        return res
    
# -----------------------------------------------------------
# 📘 Approach: Sliding Window + Hash Map with maxFreq variable
# Goal: Maximize the window size such that we can make all characters equal
#       by replacing at most `k` other characters in the window.
# 
# Use a sliding window [l, r]. At each step:
# - Count the frequency of the most frequent character in the window.
# - If the rest of the characters exceed `k`, shrink from the left.
#
# Key Condition:
# - (window size - count of max frequent char) ≤ k  → valid window
#
# Time: O(n), where n = len(s)
# Space: O(26) = O(1) → because only uppercase English letters
# -----------------------------------------------------------

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqMap = {}
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxFreq = max(maxFreq, freqMap[s[r]])

            # Window size = r - l + 1
            # Number of chars to replace = window size - maxFreq
            if (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


# -----------------------------------------------------------
# 📘 Sliding Window + Frequency Hash Map with defaultdict
# Maintain a window [l, r] and track the count of characters.
# A window is valid if: (window size - max frequency) <= k
#
# We expand the window by moving `r`, and shrink it from `l`
# if we need more than `k` changes to make all characters equal.
#
# Time: O(n), where n = len(s)
#   - Each character is processed at most twice (expand + shrink)
# Space: O(1)
#   - Max 26 uppercase letters, so hash map stays constant size
# -----------------------------------------------------------

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqMap = defaultdict(int)
        maxFreq = 0
        res = 0

        for r in range(len(s)):
            # Add the current character to the frequency map
            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            # Window size = r - l + 1
            # If more than k replacements are needed, shrink window from left
            if (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                l += 1

            # Update result with current valid window length
            res = max(res, r - l + 1)

        return res
