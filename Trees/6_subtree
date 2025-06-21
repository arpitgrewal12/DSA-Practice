"""
Problem: Subtree of Another Tree  
LeetCode: https://leetcode.com/problems/subtree-of-another-tree/

Given the roots of two binary trees root and subRoot, return True if there is a subtree of root with the 
same structure and node values as subRoot, and False otherwise.

A subtree of a binary tree is a tree that consists of a node in the tree and all of this node's descendants.
The tree itself can be considered a subtree of itself.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach: Recursive DFS with helper function sameTree()
# 1. Check if current nodes' trees are identical (sameTree).
# 2. If not, recurse on left and right subtrees of root.
# Time: O(n*m) worst case, where n = nodes in root, m = nodes in subRoot
# Space: O(m+n) recursion stack
# -----------------------------------------------------------

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is None, it is always a subtree
        if subRoot is None:
            return True
        
        # If root is None but subRoot is not, subtree can't exist
        if root is None:
            return False
        
        def sameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            return False
        
        # Check if trees rooted at current node are same
        if sameTree(root, subRoot):
            return True
        
        # Otherwise, recurse on left and right subtrees of root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
