# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        res_p, res_q = [], []
        def preorder(node, arr):
            if node:
                arr.append(node.val)
                if not node.left and not node.right:
                    return
                elif not node.left:
                    arr.append(None)
                    preorder(node.right, arr)
                elif not node.right:
                    preorder(node.left, arr)
                    arr.append(None)
                else:
                    preorder(node.left, arr)
                    preorder(node.right, arr)
            else: return
            
        preorder(p, res_p)
        preorder(q, res_q)
        return res_p == res_q