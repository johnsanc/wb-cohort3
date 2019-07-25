class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        self.targetSum(candidates, 0, target, [], results)
        return results
    
    def targetSum(self, nums, index, target_sum, path, results):
        if target_sum < 0: return
        
        elif target_sum == 0:
            results.append(path)
            return
        
        if index == len(nums): return
        
        # include the value
        path.append(nums[index])
        self.targetSum(nums, index, target_sum - nums[index], path[:], results)
        
        # exclude the value
        path.pop()
        self.targetSum(nums, index+1, target_sum, path[:], results)