from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        p_count = Counter(p)
        s_count = Counter(s[:p_len - 1])
        indeces = []
        
        for i in range(p_len-1, len(s)):
            s_count[s[i]] += 1
            if s_count == p_count:
                indeces.append(i - p_len + 1)
            s_count[s[i - p_len + 1]] -= 1
            if s_count[s[i - p_len + 1]] == 0:
                del s_count[s[i - p_len + 1]]
                
        return indeces
            