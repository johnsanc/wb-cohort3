from collections import defaultdict
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candies = set(candies)
        num_unique = len(unique_candies)
        num_candies = len(candies)
        
        if not candies:
            return 0
        
        if num_unique == num_candies:
            return num_unique // 2
        
        elif num_unique <= num_candies // 2:
            return num_unique
        
        else:
            # num_unique > num_candies // 2
            return num_candies // 2