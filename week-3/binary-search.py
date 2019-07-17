class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start, end = 0, length -1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                start = mid + 1
                
            else:
                end = mid - 1
                
        return -1
