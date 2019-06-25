class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        rowLen = len(A)
        colLen = len(A[0])
        
        if rowLen == 1 and colLen == 1:
            return A
        else:
            newList = [[0 for i in range(rowLen)] for j in range(colLen)]
            for i in range(colLen):
                for j in range(rowLen):
                    newList[i][j] = A[j][i]
                    
            return newList