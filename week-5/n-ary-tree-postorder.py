"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []
        
        def _recurse(res, node):
            for c in node.children:
                _recurse(res, c)
            result.append(node.val)
        
        if root:
            _recurse(result, root)
        return result