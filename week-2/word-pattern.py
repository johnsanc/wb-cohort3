class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_map = {}
        words = str.split()
        
        if len(words) != len(pattern):
            return False
        
        for l, w in zip(list(pattern), words):
            if l not in pattern_map.keys() and w not in pattern_map.values():
                pattern_map[l] = w
                
            elif l in pattern_map and pattern_map[l] != w:
                return False
            
            elif l not in pattern_map and w in pattern_map.values():
                return False
            
        return True