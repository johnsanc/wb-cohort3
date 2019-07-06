class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(list(J))
        counter = 0
        for s in S:
            if s in jewels:
                counter += 1
        
        return counter