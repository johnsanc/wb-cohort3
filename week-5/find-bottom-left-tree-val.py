# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        row = [root]
        
        while row:
            answer = row[0].val
            row = [child for node in row for child in (node.left, node.right) if child != None]
        return answer
            