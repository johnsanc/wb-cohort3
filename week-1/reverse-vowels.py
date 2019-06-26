class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        listStr = list(s)
        
        if not listStr:
            return s
        
        else:
            length = len(listStr)
            left = 0
            right = length - 1

            while left < right:
                while left < length and listStr[left] not in vowels:
                    left += 1
                
                while right >= 0 and listStr[right] not in vowels:
                    right -= 1
                
                if left < right:
                    lchar = listStr[left]
                    rchar = listStr[right]
                    listStr[left], listStr[right] = rchar, lchar
                    left += 1
                    right -= 1
            
            result = "".join(listStr)
            return result