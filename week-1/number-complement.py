class Solution:
    def findComplement(self, num: int) -> int:
        numBin = bin(num)[2:]
        mask = ""
        for char in range(len(numBin)):
            mask += "1"
        mask = int(mask, 2)
        
        return num ^ mask