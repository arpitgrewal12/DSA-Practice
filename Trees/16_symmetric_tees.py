"""
Problem: Symmetric Tree
LeetCode: https://leetcode.com/problems/symmetric-tree/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
"""

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach 1: DFS Recursion
# 1. Compare the left and right subtree recursively.
# 2. At each step, check:
#    - Both nodes are None → symmetric.
#    - One is None → not symmetric.
#    - Values must match.
#    - Left.left vs Right.right and Left.right vs Right.left.
# Time: O(n), Space: O(h) — height of the tree (due to call stack)
# -----------------------------------------------------------

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Edge case: empty tree is symmetric
        if root is None:
            return True

        def dfs(leftNode, rightNode):
            if not leftNode and not rightNode:
                return True
            if not leftNode or not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False

            # 🔁 Recurse into the mirror children
            return dfs(leftNode.left, rightNode.right) and dfs(leftNode.right, rightNode.left)

        return dfs(root.left, root.right)

# -----------------------------------------------------------
# 📘 Approach 2: Iterative BFS using Queue
# 1. Use a queue to compare pairs of nodes iteratively.
# 2. Push (left, right) node pairs and check for symmetry.
# Time: O(n), Space: O(n)
# -----------------------------------------------------------

class SolutionIterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            leftNode, rightNode = queue.popleft()

            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False

            # 🪞 Enqueue mirror children
            queue.append((leftNode.left, rightNode.right))
            queue.append((leftNode.right, rightNode.left))

        return True
