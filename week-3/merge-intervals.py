class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for interval in intervals:
            start, end = interval
            
            if len(result) == 0:
                result.append(interval)
            
            if result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
        
            else:
                result.append(interval)
                
        return result