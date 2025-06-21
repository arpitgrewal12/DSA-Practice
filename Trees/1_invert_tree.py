"""
Problem: Invert Binary Tree
LeetCode: https://leetcode.com/problems/invert-binary-tree/

You are given the root of a binary tree.
Invert the binary tree and return its root.
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
# 📘 Approach 1: Recursive DFS with a New Tree
# Creates a new tree with left/right children swapped
# Time: O(n), Space: O(n)
# -----------------------------------------------------------

class SolutionNewTree:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        new_node = TreeNode(root.val)
        new_node.left = self.invertTree(root.right)
        new_node.right = self.invertTree(root.left)

        return new_node


# -----------------------------------------------------------
# 📘 Approach 2: In-Place Recursive DFS
# Swaps the children at each node directly
# Time: O(n), Space: O(h) where h is height of tree
# -----------------------------------------------------------

class SolutionInPlace:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        # Having the below code in one line is important else we will
        # have to use a temp variable to swap cause we dont want to change the values
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# -----------------------------------------------------------
# 📘 Approach 3: Iterative BFS using Queue
# Level-order traversal and swap children
# Time: O(n), Space: O(w) where w = max width of tree
# -----------------------------------------------------------

class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])

        while queue:
            node = queue.popleft()
            # Swap children

            node.left, node.right = node.right, node.left
            # Remember we are doing travesal left to right so order is important

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root
