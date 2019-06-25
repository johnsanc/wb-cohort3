class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        lenCol = len(A[0])
        lenRow = len(A)
        result = []
        for i in range(lenRow):
            A[i].reverse()
            result.append(A[i])
        
        for i in range(lenRow):
            for j in range(lenCol):
                result[i][j] ^= 1
                    
        return result