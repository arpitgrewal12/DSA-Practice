"""
Problem: Count Good Nodes in Binary Tree  
LeetCode: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

A node X in the binary tree is named "good" if in the path from root to X 
there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach 1: DFS with class-level counter
# 1. Traverse the tree from root to leaves (pre-order).
# 2. Keep track of the maximum value seen so far on the current path.
# 3. If current node's value >= current max → it's a good node.
# Time: O(n), Space: O(h) where h = height of the tree (due to recursion)
# -----------------------------------------------------------

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Edge case: empty tree
        if root is None:
            return 0

        self.count = 0  # To store the number of good nodes

        def dfs(node, curr_max):
            if node is None:
                return

            # If current node is good
            if node.val >= curr_max:
                self.count += 1
                curr_max = node.val  # Update max for the current path

            # 🔍 Note:
            # curr_max is passed down by value (integers are immutable in Python)
            # So left and right paths manage their own version of curr_max

            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        # Start DFS traversal from root
        dfs(root, root.val)
        return self.count


# -----------------------------------------------------------
# 📘 Approach 2: DFS with return value (functional style)
# No class variables — pure function-style DFS with return value
# -----------------------------------------------------------

class SolutionPure:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if node is None:
                return 0

            # Count 1 if current node is good
            good = 1 if node.val >= curr_max else 0
            curr_max = max(curr_max, node.val)

            # Recurse into left and right
            left = dfs(node.left, curr_max)
            right = dfs(node.right, curr_max)

            return good + left + right

        return dfs(root, root.val)
