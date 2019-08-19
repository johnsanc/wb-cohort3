# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = []
        
        def mod_preorder(node, arr, isLeft):
            # first iteration will be root
            if node:
                if isLeft and not node.left and not node.right:
                    arr.append(node.val)
                mod_preorder(node.left, arr, True)
                mod_preorder(node.right, arr, False)
            else: return
        
        mod_preorder(root, res, False)
        return sum(res)