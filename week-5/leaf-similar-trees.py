# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        res1, res2 = [], []
        
        def _recurse(node, arr):
            if node:
                if not node.left and not node.right:
                    arr.append(node.val)
                _recurse(node.left, arr)
                _recurse(node.right, arr)
            else: return
        
        _recurse(root1, res1)
        _recurse(root2, res2)
        
        return res1 == res2