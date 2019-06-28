from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        
        for letter in s:
            s_dict[letter] += 1
        
        for char in t:
            t_dict[char] += 1
            
        return s_dict == t_dict