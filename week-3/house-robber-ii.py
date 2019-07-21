class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if not nums:
            return 0
        
        if length == 1:
            return nums[0]
        
        prev = curr = 0
        a = b = 0
        # Don't include the last value, include first
        for i in range(length -1):
            prev, curr = curr, max(prev + nums[i], curr)
            
        a = curr
        
        prev = curr = 0 #reset
        # exclude first value, include last
        for i in range(1, length):
            prev, curr = curr, max(prev + nums[i], curr)
            
        b = curr
        
        return max(a,b)