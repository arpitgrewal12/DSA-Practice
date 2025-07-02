"""
Problem: Valid Palindrome
LeetCode: https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

-----------------------------------------------------------
🔍 Logic:
- Use two pointers, `l` (left) and `r` (right), starting at the beginning and end of the string.
- Move `l` forward and `r` backward, skipping non-alphanumeric characters using helper function `isAlphaNumeric`.
- Compare characters at `l` and `r` ignoring case.
- If mismatch found, return False; if pointers cross, return True.

-----------------------------------------------------------
Python `ord()` function:
- `ord(char)` returns the Unicode code point (integer) for the given character `char`.
- Example: `ord('a')` returns 97, `ord('Z')` returns 90.
- Used here to check if characters fall within ASCII ranges for digits and letters.

-----------------------------------------------------------
Time Complexity: O(n)
- Each character is visited at most once by the two pointers.

Space Complexity: O(1)
- Only constant extra space used for pointers and variables.
-----------------------------------------------------------
🔍 Logic to Skip Non-Alphanumeric Characters:

There are two common approaches to skip non-alphanumeric characters when checking palindrome:

1️⃣ Using Two Inner `while` Loops:

- For each iteration, skip all consecutive non-alphanumeric characters at once on both sides (left and right pointers).
- Efficiently jumps over multiple non-alphanumeric chars in a single iteration.

Example:
s = "a,, ,b"
- Left pointer `l` at 'a' (alphanumeric), no skip.
- Right pointer `r` skips all commas/spaces until reaching 'b'.

2️⃣ Using Single `if` Checks with `continue`:

- On each iteration, check if current left or right pointer points to non-alphanumeric character.
- If yes, skip one character and continue to next iteration.
- Skips non-alphanumeric chars one by one, potentially more iterations.

Example:
s = "a,, ,b"
- Multiple iterations to skip each comma or space individually on the right pointer.

-----------------------------------------------------------
| Approach                 | Skips Multiple Non-Alphanumerics Per Iteration? | Number of Loop Iterations |
|--------------------------|-------------------------------------------------|---------------------------|
| Two inner `while` loops  | Yes                                             | Fewer                     |
| Single `if` + `continue` | No                                              | More                      |

Both produce correct results, but two inner `while` loops are more efficient in practice.
-----------------------------------------------------------
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            # Skip non-alphanumeric characters from the right
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            
            # Compare lowercase characters
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True

    def isAlphaNumeric(self, c: str) -> bool:
        # Check if character is alphanumeric by comparing Unicode code points using ord()
        return (
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9')
        )
