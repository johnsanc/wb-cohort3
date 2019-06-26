class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xBin = bin(x)[2:]
        yBin = bin(y)[2:]
        xLen = len(xBin)
        yLen = len(yBin)
        
        # Make both strings the same length
        if xLen < yLen:
            zeros = ""
            for _ in range(yLen-xLen):
                zeros += "0"
            temp = zeros + xBin
            xBin = temp
        
        elif yLen < xLen:
            zeros = ""
            for _ in range(xLen-yLen):
                zeros += "0"
            temp = zeros + yBin
            yBin = temp
        
        if len(xBin) <= 2:
            if xBin != yBin:
                return 1
            
        # track the start and end pointers
        start, stop = 0, 0
        for i in range(len(xBin) - 1, -1, -1):
            if xBin[i] != yBin[i]:
                start = i
                break
        for j in range(start - 1, -1, -1):
            if xBin[j] != yBin[j]:
                stop = j
                #break
        
        # calculate distance
        counter = 0
        for i in range(start, stop - 1, -1):
            if xBin[i] != yBin[i]:
                counter += 1
        
        return counter