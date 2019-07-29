class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        paths = []
        self.combinations(nums, 0, len(nums) - 1, paths)
        return paths
    
    def combinations(self, num_list, start, stop, results):
        if start == stop:
            results.append(num_list[:])
            return
        
        else:
            for i in range(start, stop+1):
                num_list[start], num_list[i] = num_list[i], num_list[start]
                self.combinations(num_list, start+1, stop, results)
                num_list[start], num_list[i] = num_list[i], num_list[start]