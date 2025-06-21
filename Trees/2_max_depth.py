"""
Problem: Maximum Depth of Binary Tree  
LeetCode: https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path 
from the root node down to the farthest leaf node.
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
# Computes the depth by taking the max of left and right subtree depths
# Time: O(n), Space: O(h) where h = height of tree (due to recursion stack)
# -----------------------------------------------------------

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)

        return 1 + max(leftHeight, rightHeight)
