"""
Problem: Same Tree  
LeetCode: https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, return True if the trees are identical in structure and node values.

Two binary trees are considered the same if they have the same structure and the same node values.
"""

from typing import Optional
from collections import deque  # ✅ Needed for the BFS approach

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach 1: Recursive DFS
# Compares structure and node values at each corresponding position
# Time: O(n), Space: O(h) where n = number of nodes, h = tree height
# -----------------------------------------------------------

class SolutionRecursive:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        
        return False


# -----------------------------------------------------------
# 📘 Approach 2: Iterative BFS using Queue
# Compare corresponding nodes in both trees in parallel
# Time: O(n), Space: O(n)
# In the worst case, the queue can hold up to all nodes at the largest level of the trees simultaneously
# -----------------------------------------------------------

class SolutionIterative:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])

        while queue:
            node1, node2 = queue.popleft()

            if not node1 and not node2:
                continue

            if not node1 or not node2 or node1.val != node2.val:
                return False

            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))

        return True
