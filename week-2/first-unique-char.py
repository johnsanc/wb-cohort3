from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_count = Counter(s)
        unique = []
        
        for key,val in s_count.items():
            if val == 1:
                unique.append(key)
        
        first = len(s)
        if not unique:
            return -1
        
        for val in unique:
            first = min(s.index(val), first)
        
        return first