class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        len1 = len(word1)
        len2 = len(word2)
        
        return self.minDistance_helper(word1, word2, len1, len2)
    
    def minDistance_helper(self, string1, string2, length1, length2):
        
        if length1 == 0:
            return length2
        
        elif length2 == 0:
            return length1
        
        elif string1[length1-1] == string2[length2-1]:
            return self.minDistance_helper(string1, string2, length1-1, length2-1)
        
        else:
            return min(self.minDistance_helper(string1, string2, length1-1, length2),
                       self.minDistance_helper(string1, string2, length1-1, length2-1),
                       self.minDistance_helper(string1, string2, length1, length2-1)) + 1