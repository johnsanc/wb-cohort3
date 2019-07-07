class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        
        for i in range(len(s)): 
            if s[i] not in mapping_s:
                mapping_s[s[i]] = t[i]
            if s[i] in mapping_s and mapping_s[s[i]] != t[i]:
                return False
            
        for j in range(len(t)):
            if t[j] not in mapping_t:
                mapping_t[t[j]] = s[j]
            if t[j] in mapping_t and mapping_t[t[j]] != s[j]:
                    return False
                                
        return True