"""
Problem: Binary Tree Level Order Traversal  
LeetCode: https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values.
(From left to right, level by level).
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
# 📘 Approach 1: Iterative BFS using a Queue
# 1. Use a queue to traverse level-by-level.
# 2. For each level, store all node values in a list.
# 3. Push left/right children to the queue for next level.
# Time: O(n), Space: O(n), where n is number of nodes
# -----------------------------------------------------------

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: if the tree is empty, return an empty list
        if root is None: 
            return []
        
        result = []  # Final result: list of levels, each containing node values
        queue = deque([root])  # Queue for BFS traversal, initialized with root

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_nodes = []         # List to store values of nodes at this level

            for _ in range(level_size):
                node = queue.popleft()  # Pop the current node from the front of the queue

                # Add child nodes to the queue for next level processing
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                level_nodes.append(node.val)  # Store the current node's value

            result.append(level_nodes)  # Add current level's values to result
        
        return result  # Return the complete level order traversal


# -----------------------------------------------------------
# 📘 Approach 2: Recursive DFS (Top-down)
# 1. Use DFS with level tracking.
# 2. Maintain a result list where each index corresponds to a level.
# 3. Add node values to the correct level list during traversal.
# Time: O(n), Space: O(n)
# -----------------------------------------------------------

class SolutionDFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, level):
            if not node:
                return
            
            # If encountering this level for the first time, add a new list
            if level == len(result):
                result.append([])

            # Append current node value to its level list
            result[level].append(node.val)

            # Recurse for left and right subtrees
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return result
