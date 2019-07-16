class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=sort_second)
        start = points[0][1]
        num_arrows = 1
        length = len(points)
        
        for i in range(1,length):
            if start >= points[i][0]:
                continue
            num_arrows += 1
            start = points[i][1]
        return num_arrows
    
def sort_second(pair):
    return pair[1]