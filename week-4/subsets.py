class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.combinations(nums, 0)
    
    def combinations(self, arr, index):
        
        length = len(arr)
        
        if index == length:
            return [[]]
        
        result = []
        
        for subset in self.combinations(arr, index + 1):
            # exclude the item
            result.append(subset)
            
            # include the item
            copy = subset[:]
            copy.insert(0, arr[index])
            result.append(copy)
            
        return result