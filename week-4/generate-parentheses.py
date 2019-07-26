class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.combinations(n, n, "", [])
        
    
    def combinations(self, left, right, path, result):
        if left > 0:
            self.combinations(left-1, right, path+'(', result)
        if right > left:
            self.combinations(left, right-1, path+')', result)
        if right == 0:
            result.append(path)
        return result