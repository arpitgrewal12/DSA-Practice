"""
Problem: Serialize and Deserialize Binary Tree  
LeetCode: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

You need to serialize a binary tree into a string and then deserialize it back to the original structure.

Approach:
📘 Use Preorder DFS (Root → Left → Right) for both serialization and deserialization.
- Represent null nodes with "N" to preserve structure.
- Use a comma to separate values in the string.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    # -----------------------------------------------------------
    # ✅ Serialize: Preorder DFS
    # Time: O(n) — visit every node once
    # Space: O(n) — recursion stack + result list
    # -----------------------------------------------------------
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if node is None:
                res.append("N")  # Use "N" to mark null
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # -----------------------------------------------------------
    # ✅ Deserialize: Rebuild using Preorder
    # Time: O(n) — process each value exactly once
    # Space: O(n) — recursion stack
    # -----------------------------------------------------------
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.idx = 0  # initialize index counter

        def dfs():
            if vals[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(vals[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
