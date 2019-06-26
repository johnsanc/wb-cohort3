class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        result = []
        for word in words:
            temp = list(word)
            temp.reverse()
            word = "".join(temp)
            result.append(word)
            
        return " ".join(result)