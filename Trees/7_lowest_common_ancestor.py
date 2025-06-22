"""
Problem: Lowest Common Ancestor of a Binary Search Tree  
LeetCode: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

Definition: The lowest common ancestor is the lowest node in the tree that has both p and q as descendants 
(where a node can be a descendant of itself).
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Recursive DFS Approach
# 1. Traverse using BST rules.
# 2. If both p and q are less than current node → search left subtree.
# 3. If both are greater → search right subtree.
# 4. Else, split point found — this node is the LCA.
# Time: O(h), Space: O(h) due to recursion
# -----------------------------------------------------------

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base case: null root
        if root is None:
            return None

        # If current node is the split point or one of the target nodes, it's the LCA
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root

        # Both nodes lie in the left subtree
        elif max(p.val, q.val) < root.val:
            # ⚠️ The return is crucial — we need to return what the recursive call gives us
            return self.lowestCommonAncestor(root.left, p, q)

        # Both nodes lie in the right subtree
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)


# -----------------------------------------------------------
# 📘 Iterative Approach
# 1. Same logic as DFS, but use a loop instead of recursion.
# 2. Traverse from root, update pointer according to BST rules.
# 3. Stop when split point is found.
# Time: O(h), Space: O(1)
# -----------------------------------------------------------

class SolutionIterative:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # Move to left subtree if both values are smaller
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left

            # Move to right subtree if both values are greater
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right

            # Found the split point (or exact match)
            else:
                return curr
