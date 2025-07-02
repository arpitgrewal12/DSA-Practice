"""
Problem: Encode and Decode Strings
LeetCode: https://leetcode.com/problems/encode-and-decode-strings/

Design an algorithm to encode a list of strings to a single string,
and decode it back to the original list.

-----------------------------------------------------------
🔍 Logic:
- For encoding, use a length-prefixed format: <length>#<string>
  - This makes it safe even if the string contains special characters like '#'.
  - Example: ["neet", "code", "you"] → "4#neet4#code3#you"

- For decoding:
  - Read characters until you find a '#'
  - The substring before '#' is the length of the word
  - Extract the next `length` characters as the actual word
  - Move forward and repeat

-----------------------------------------------------------
Time complexity: 
O(m)
O(m) for each encode() and decode() function calls.

Reasoning:  
- The encode function loops over the list of strings (m strings) and processes each string.
- The decode function loops over the encoded string, parsing each encoded segment once.
- Since each string is handled once, the complexity is proportional to the number of strings m.

Space complexity: 
O(m + n)
O(m + n) for each encode() and decode() function calls.

Reasoning:
- The space to store the encoded string or the decoded list includes:
  - m: number of strings in the list (metadata like lengths, and list overhead)
  - n: total length of all characters across all strings
- Thus, total space grows linearly with both the number of strings and their total size.
-----------------------------------------------------------
"""

from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            # Append length of the string + '#' delimiter + actual string
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        myList = []
        i = 0

        while i < len(s):
            j = i
            # Move j to find the '#' character
            while s[j] != "#":
                j += 1

            # Get the number before '#' → length of word
            length = int(s[i:j])

            # Get the actual word from j+1 to j+1+length
            word = s[j + 1 : j + 1 + length]
            myList.append(word)

            # Move i to the start of the next encoded segment
            i = j + 1 + length

        return myList
