"""
Problem: Kth Smallest Element in a BST  
LeetCode: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree (BST) and an integer k, return the kth smallest value
(1-indexed) among all the values of the nodes in the tree.

A BST's in-order traversal gives nodes in sorted order, so the kth element of an in-order traversal is the answer.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach 1: In-order DFS traversal with result array
# 1. Perform in-order traversal (Left → Node → Right) on BST.
# 2. Collect node values in a list as they appear.
# 3. Return the (k-1)th value from the list (0-indexed).
# Time: O(n), Space: O(n)
# -----------------------------------------------------------

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = []

        def dfs(node):
            if node is None:
                return

            # Traverse left subtree
            dfs(node.left)

            # Visit current node
            self.result.append(node.val)

            # Traverse right subtree
            dfs(node.right)

        dfs(root)
        return self.result[k - 1]
