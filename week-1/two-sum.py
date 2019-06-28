class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        matches = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in matches:
                return [matches[diff], i]
            matches[nums[i]] = i
        return []