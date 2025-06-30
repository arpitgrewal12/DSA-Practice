"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal  
LeetCode: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal 
of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
"""

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -----------------------------------------------------------
# 📘 Naive Approach: Recursive with slicing
#
# fact 1: The first node in preorder traversal is always the root.
# fact 2: Once we know the root, we can split inorder into two subtrees:
#         - Left subtree = elements before the root
#         - Right subtree = elements after the root
# fact 3: Length of left subtree in inorder lets us split preorder
#         into left and right subtrees accordingly.
# fact 4: We then recursively build the tree using slices.
#
# ❌ Inefficient: list slicing creates new arrays (O(n) per slice)
# ❌ Also uses inorder.index() = O(n) per call
#
# ✅ Time Complexity: O(n²) in worst case (e.g. skewed tree)
# ✅ Space Complexity: O(n²) due to slicing overhead and recursion stack
# -----------------------------------------------------------

class SolutionNaive:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root


# -----------------------------------------------------------
# 📘 Optimized Approach: Recursive DFS with index map
#
# ✅ Same logic as above, but no slicing.
# ✅ Use a hashmap to store index of each value in inorder.
# ✅ Use preorder.pop(0) to simulate moving forward in preorder.
#
# 🚫 preorder.pop(0) is O(n), but Python list pops from front can be replaced
#    with deque for O(1). Still accepted for simplicity here.
#
# ✅ Time Complexity: O(n)
#     - Each node processed once
#     - Index lookups in O(1) due to map
# ✅ Space Complexity: O(n)
#     - Recursion stack for tree height (O(h))
#     - Hashmap storage = O(n)
# -----------------------------------------------------------

class SolutionOptimized:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}

        def dfs(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            index = inorder_index[root_val]

            root.left = dfs(in_left, index - 1)
            root.right = dfs(index + 1, in_right)

            return root

        return dfs(0, len(inorder) - 1)


# -----------------------------------------------------------
# 📘 Postorder + Inorder Approach
#
# Problem: Construct Binary Tree from Inorder and Postorder Traversal  
# LeetCode: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
#
# 🔁 postorder = Left → Right → Root
# ✅ postorder[-1] is always the root
# ✅ Recursively build:
#     - Right subtree first (since postorder is popped from end)
#     - Then left subtree
#
# ✅ Time Complexity: O(n)
#     - Each node processed once
#     - Index lookups in O(1) via hashmap
# ✅ Space Complexity: O(n)
#     - Recursion stack + hashmap
# -----------------------------------------------------------

class SolutionPostorder:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}

        def dfs(in_left, in_right):
            if in_left > in_right:
                return None

            root_val = postorder.pop()
            root = TreeNode(root_val)

            index = inorder_index[root_val]

            root.right = dfs(index + 1, in_right)
            root.left = dfs(in_left, index - 1)

            return root

        return dfs(0, len(inorder) - 1)
