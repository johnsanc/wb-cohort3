class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        happy_campers = 0
        child, cookie = 0, 0
        
        g.sort()
        s.sort()
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                happy_campers += 1
                child += 1
            cookie += 1
        
        return happy_campers