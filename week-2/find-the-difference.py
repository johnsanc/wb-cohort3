from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)
        len_s = len(s)
        len_t = len(t)
        
        if len_s < len_t:
            for item, val in count_t.items():
                if count_s[item] != count_t[item]:
                    return item
        
        if len_s > len_t or len_s == len_t:
            for item, val in count_s.items():
                if count_t[item] != count_s[item]:
                    return item
        