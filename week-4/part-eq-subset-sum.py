class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        lookup = {}
        
        if sum(nums) % 2:
            return False
        
        return self.partition(nums, 0, sum(nums)//2, lookup)
    
    def partition(self, numbers, start, total, lookup):
        if (start,total) in lookup:
            return lookup[(start,total)]
        if total < 0: return False
        elif total == 0: return True
        
        for i in range(start, len(numbers)):
            if self.partition(numbers, i+1, total-numbers[i], lookup) or self.partition(numbers, i+1, total, lookup):
                return True
            lookup[(start,total)] = False
            return False
        