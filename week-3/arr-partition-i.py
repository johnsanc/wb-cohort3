class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        
        for i in range(1, len(nums), 2):
            result += min(nums[i-1], nums[i])
            
        return result