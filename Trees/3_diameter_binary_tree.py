"""
Problem: Diameter of Binary Tree  
LeetCode: https://leetcode.com/problems/diameter-of-binary-tree/

The diameter of a binary tree is defined as the length of the longest path between any two nodes in the tree. 
This path may or may not pass through the root. The length is measured by the number of edges between nodes.

Given the root of a binary tree, return its diameter.
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
# At each node, diameter is the sum of left and right subtree heights
# Use a class-level variable to track the max diameter
# Time: O(n), Space: O(h) where h = height of the tree
# -----------------------------------------------------------

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # Tracks the max diameter found so far

        def maxHeight(node):
            if node is None:
                return 0
            
            leftHt = maxHeight(node.left)
            rightHt = maxHeight(node.right)

            # Update the diameter if the path through this node is longer
            self.diameter = max(self.diameter, leftHt + rightHt)

            # Return the height of the current node
            return 1 + max(leftHt, rightHt)
        
        maxHeight(root)
        return self.diameter
