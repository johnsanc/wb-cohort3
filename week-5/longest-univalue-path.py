# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.longest = 0
        
        def find_length(node, val):
            if not node: return 0
            
            left, right = find_length(node.left, node.val), find_length(node.right, node.val)
            self.longest = max(self.longest, left + right)
            if node.val == val:
                return 1 + max(left, right)
            else:
                return 0
            
        find_length(root, None)
        
        return self.longest