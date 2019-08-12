class Solution:
    def grayCode(self, n: int) -> List[int]:
        nums = [0]
        
        for i in range(n):
            nums += [x+pow(2,i) for x in reversed(nums)]
            
        return nums