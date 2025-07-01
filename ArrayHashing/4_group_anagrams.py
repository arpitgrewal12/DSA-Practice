"""
Problem: Group Anagrams
LeetCode: https://leetcode.com/problems/group-anagrams/

Given an array of strings `strs`, group the anagrams together.
Return a list of groups, where each group contains strings that are anagrams of each other.

Anagrams are strings made up of the same characters in different orders.
"""

from typing import List
from collections import defaultdict

# -----------------------------------------------------------
# 📘 Approach: Sort Each Word to Use as Key
# Sort each string and use the sorted version as a key in a hashmap.
# Anagrams will have the same sorted form, so they group together.
# Time: O(n * k log k), Space: O(n * k)
#     - n = number of strings
#     - k = max length of a string (due to sorting)
# -----------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dictionary where each value is a list
        # This will map sorted words (as keys) to lists of anagrams
        anagram_map = defaultdict(list)
        
        # Iterate over each word in the input list
        for s in strs:
            # Sort the characters in the word to get the anagram key
            # For example, 'eat' -> 'aet', 'tea' -> 'aet'
            key = ''.join(sorted(s))
            
            # Append the original word to the list corresponding to this key
            anagram_map[key].append(s)
        
        # Convert the dictionary values to a list of lists and return it
        return list(anagram_map.values())

# -----------------------------------------------------------
# 📘 Approach 2: Hash Map with Character Frequency Count as Key
# Instead of sorting each string (which takes O(k log k) time), 
# count the frequency of each character (a-z) in O(k) time.
# Use a tuple of counts as a hashable key to group anagrams.
# 
# Time Complexity: O(n * k)
#   - n = number of strings
#   - k = max length of a string
# Space Complexity: O(n * k) for storing groups and keys
# -----------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams keyed by character frequency tuple
        res = defaultdict(list)

        for word in strs:
            # Initialize a frequency count list for 26 lowercase letters
            count = [0] * 26
            
            # Count the occurrences of each character in the word
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            # Convert the frequency list eg [0,1,0,....] to a tuple (0,1,0,......) to use as a dictionary key
            key = tuple(count)
            
            # Append the original word to the list corresponding to this frequency key
            res[key].append(word)

        # Return the grouped anagrams as a list of lists
        return list(res.values())


# -----------------------------------------------------------
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
#
# Explanation:
# - "eat", "tea", and "ate" all have the same character counts.
# - "tan" and "nat" are anagrams of each other.
# - "bat" is alone since it doesn't have an anagram in the list.
# -----------------------------------------------------------