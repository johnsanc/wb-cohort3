from collections import defaultdict
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        
        if n == 1:
            return True
        
        squares = defaultdict(int)
        for i in range(10):
            squares[i] = i**2
        
        is_happy = False
        
        while n > 1:
            # go through all digits in n
            sum_squares = 0
            for d in str(n):
                sum_squares += squares[int(d)]
            n = sum_squares
            if n == 4:
                break
        
        if n == 1:
            is_happy = True
        
        return is_happy