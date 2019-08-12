class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or not k:
            return False
        
        length = len(nums)
        num_sum = sum(nums)
        if length < k or num_sum % k:
            return False
        
        used = [False for _ in range(length)]
        
        def partition(start, numbers, used, k, curr_sum, target_sum):
            if k == 1:
                return True
            
            if curr_sum == target_sum:
                return partition(0, numbers, used, k-1, 0, target_sum)
            
            for i in range(start, length):
                if not used[i]:
                    used[i] = True
                    
                    if partition(i+1, numbers, used, k, curr_sum + numbers[i], target_sum):
                        return True
                
                    used[i] = False
            
            return False
        
        return partition(0, nums, used, k, 0, num_sum // k)