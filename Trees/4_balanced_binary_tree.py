"""
Problem: Balanced Binary Tree  
LeetCode: https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, return True if it is height-balanced and False otherwise.

A height-balanced binary tree is defined as one in which the left and right subtrees 
of every node differ in height by no more than 1.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach: Recursive DFS (Post-order traversal)
# Calculates height while checking balance at each node
# Time: O(n), Space: O(h) where h = height of tree
# -----------------------------------------------------------

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        self.flag = True  # Tracks if the tree is balanced

        def dfs(node):
            if node is None:
                return 0

            leftHt = dfs(node.left)
            rightHt = dfs(node.right)

            if abs(leftHt - rightHt) > 1:
                self.flag = False

            return 1 + max(leftHt, rightHt)
        
        dfs(root)
        return self.flag
