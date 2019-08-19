# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.length = 0
        def _get_length(node):
            if node:
                left = _get_length(node.left)
                right = _get_length(node.right)
                self.length = max(self.length, left + right)
                return 1 + max(left, right)
            else: return 0
        
        _get_length(root)
        return self.length