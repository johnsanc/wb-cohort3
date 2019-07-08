from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        count = Counter(nums)
        result = []
        
        for key,val in sorted(count.items()):
            if val > 1 and key-1 > 0 and count[key-1] == 0:
                result.append(key)
                result.append(key-1)
                return result
            elif val > 1 and count[key + 1] == 0:
                result.append(key)
                result.append(key+1)
                return result
            
            elif val > 1:
                for i in range(1, len(nums) + 1):
                    if count[i] == 0:
                        result.append(key)
                        result.append(i)
        return result