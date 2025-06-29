"""
Problem: Validate Binary Search Tree  
LeetCode: https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A BST is valid if:
- For every node, all nodes in the left subtree are less than the node's value,
- and all nodes in the right subtree are greater than the node's value.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach: DFS with value bounds (Pre-order style)
# 1. Start with the full valid range: (-inf, +inf).
# 2. For each node, check if its value is within (left, right) bounds.
# 3. Recursively narrow the bounds:
#    - For left child: valid range becomes (left, node.val)
#    - For right child: valid range becomes (node.val, right)
# 4. Return False if any node violates the rule.
# Time: O(n), Space: O(h) where h = tree height
# -----------------------------------------------------------

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            if node is None:
                return True

            # If current node violates the valid range
            if node.val <= left or node.val >= right:
                return False

            # Check left and right subtrees with updated bounds
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float('-inf'), float('inf'))
