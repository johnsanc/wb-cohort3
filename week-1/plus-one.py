class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strInt = ""
        for num in digits:
            strInt += str(num)
        
        resNum = int(strInt) + 1
        resNum = str(resNum)
        final = []
        for num in resNum:
            final.append(int(num))
        
        return final 