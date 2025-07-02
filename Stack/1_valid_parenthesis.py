"""
Problem: Valid Parentheses
LeetCode: https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
"""

from typing import List

# -----------------------------------------------------------
# 📘 Approach 1: Stack + HashMap for matching pairs
# - Use a stack to keep track of opening brackets.
# - When encountering a closing bracket, check if it matches the last opening bracket.
# - If it matches, pop from the stack.
# - Else, return False.
# - In the end, if stack is empty, return True.
#
# Time: O(n) — one pass through string
# Space: O(n) — stack in worst case stores all opening brackets
# -----------------------------------------------------------

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Approach 1: Using a stack and a hashmap for matching pairs

        Logic:
        - Traverse each character in the string.
        - If the character is a closing bracket, check if the top of the stack
          is the corresponding opening bracket.
          - If yes, pop from the stack.
          - Else, return False.
        - If the character is an opening bracket, push it onto the stack.
        - At the end, if the stack is empty, all brackets matched correctly.

        Time Complexity: O(n), where n = length of string s.
        Space Complexity: O(n), for the stack in worst case.
        """

        myStack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{" }

        for c in s:
            if c in closeToOpen:
                # Current character is a closing bracket
                # Check if stack is non-empty and top matches corresponding open bracket
                if myStack and myStack[-1] == closeToOpen[c]:
                    myStack.pop()  # valid pair found, pop it
                else:
                    return False  # invalid closing bracket or mismatch
            else:
                # Current character is an opening bracket, push to stack
                myStack.append(c)

        # If stack empty, all brackets matched correctly
        return len(myStack) == 0



# -----------------------------------------------------------
# 📘 Approach 2: Manual bracket matching without hashmap
# - Use stack to store opening brackets.
# - For each closing bracket, check manually if top of stack matches.
# - Pop if matches, else return False.
# - Push opening brackets.
# - Return True if stack empty at end.
#
# Time: O(n)
# Space: O(n)
# -----------------------------------------------------------

class SolutionAlt:
    def isValid(self, s: str) -> bool:
        """
        Logic:
        - Use a stack to store opening brackets.
        - For each closing bracket, check top of stack manually for matching opening bracket.
        - If match, pop; else return False.
        - Push opening brackets when encountered.
        - Return True if stack empty at end.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """

        myStack = []

        for char in s:
            if char == '}' and myStack and myStack[-1] == '{':
                myStack.pop()
            elif char == ']' and myStack and myStack[-1] == '[':
                myStack.pop()
            elif char == ')' and myStack and myStack[-1] == '(':
                myStack.pop()
            else:
                # For opening brackets or unmatched closing brackets
                myStack.append(char)

        return len(myStack) == 0
