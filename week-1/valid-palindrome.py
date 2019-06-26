class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaString = ""
        
        for char in s.lower():
            if char.isalpha() or char.isnumeric():
                alphaString += char
                
        return alphaString == alphaString[::-1]