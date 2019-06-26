import math
class Solution:
    def titleToNumber(self, s: str) -> int:
        lettersLen = len(s)
        
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        values = {}
        
        for i, letter in enumerate(alphabet, 1):
            values[letter] = i
            
        length = len(s)
        
        if length == 0:
            return s
        elif length == 1:
            return values[s]
        else:
            result = 0
            
            for i in range(length - 1):
                result += math.pow(26, length - 1 - i) * values[s[i]]
            
            result += values[s[length - 1]]
            
            return int(result)