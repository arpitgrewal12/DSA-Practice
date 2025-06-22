"""
Problem: Binary Tree Right Side View  
LeetCode: https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, return the values of the nodes you can see 
ordered from top to bottom when looking at the tree from the right side.
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# -----------------------------------------------------------
# 📘 Approach 1: Level-order BFS
# 1. Traverse the tree level by level using a queue.
# 2. At each level, collect all node values.
# 3. The last node at each level is the visible one from the right.
# Time: O(n), Space: O(n)
# -----------------------------------------------------------

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])  # Queue for level-order traversal
        res = []  # Stores rightmost elements of each level

        while queue:
            level_size = len(queue)
            node_list = []

            for _ in range(level_size):
                node = queue.popleft()
                node_list.append(node.val)

                # Enqueue left and right children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # The last node in node_list is the rightmost at this level
            res.append(node_list[-1])

        return res


# -----------------------------------------------------------
# 📘 Approach 2: DFS (Right-first traversal)
# 1. Traverse the tree in root → right → left order.
# 2. Keep track of the current depth (level).
# 3. If this is the first time reaching a level, add the node to the result.
# Time: O(n), Space: O(h) where h = height of the tree (due to recursion)
# -----------------------------------------------------------

class SolutionDFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, level):
            if not node:
                return

            # If visiting the level for the first time, add the first node (rightmost)
            if level == len(result):
                result.append(node.val)

            # Visit right before left
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 0)
        return result
