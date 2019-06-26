class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        
        short_str = min(strs, key=len)
        
        for i, char in enumerate(short_str):
            for word in strs:
                if word[i] != char:
                    return short_str[:i]
            
        return short_str