class Solution:
    def binaryGap(self, N: int) -> int:
        # Get binary representation
        numBin = list(bin(N)[2:])
        
        onesIndeces = []
        length = len(numBin)
        distance = 0
        
        for i in range(length):
            if numBin[i] == "1":
                onesIndeces.append(i)
        
        for i in range(len(onesIndeces) - 1):
            distance = max(distance, onesIndeces[i + 1] - onesIndeces[i])
        
        return distance