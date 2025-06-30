"""
Problem: Populating Next Right Pointers in Each Node  
LeetCode: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a **perfect binary tree** (every internal node has two children and all leaves are at the same level).
Your task is to connect each node's `next` pointer to its right neighbor.
If there is no right neighbor, the `next` pointer should be set to NULL.

Initially, all next pointers are set to NULL.
"""

# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

# -----------------------------------------------------------
# 📘 Approach: Recursive DFS leveraging perfect binary tree structure
# 
# ✨ Key Observations:
# 1. In a perfect binary tree:
#     - node.left exists if node.right exists
#     - all leaves are at the same level
# 2. We only need to link:
#     - node.left.next = node.right
#     - node.right.next = node.next.left (if node.next exists)
#
# 🔁 We recursively connect left and right children
#
# ✅ Time Complexity: O(n)
#     - Each node is visited once
# ✅ Space Complexity: O(h)
#     - Recursion stack = height of the tree
#     - O(log n) for balanced/perfect trees
# -----------------------------------------------------------

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        
        def dfs(node):
            # Base case: if node is a leaf or null, stop
            if node is None or node.left is None:
                return

            # Connect left child → right child
            node.left.next = node.right

            # Connect right child → next node’s left child (if exists)
            if node.next:
                node.right.next = node.next.left

            # Recurse into children
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return root


# -----------------------------------------------------------
# 📘 Approach: Level Order Traversal (BFS) using a Queue
#
# ✅ Idea:
# - Traverse level-by-level using a queue
# - At each level, connect nodes from left to right using a pointer
#
# ✅ Steps:
# 1. Add root to the queue.
# 2. For each level:
#     - Iterate through all nodes in that level.
#     - Use a `prev` pointer to connect node.prev.next = node.
#
# ✅ Time Complexity: O(n)
#     - Each node is visited once
# ✅ Space Complexity: O(n)
#     - Queue stores all nodes at one level (worst case: n/2)
# -----------------------------------------------------------
from collections import deque

class Solution:
    def connect(self, root):
        if root is None:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()

                if prev:
                    prev.next = node
                prev = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root
