import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1 or n == 2:
            return True
        elif n <= 0:
            return False
        else:
            exponent = int(math.log(n, 2))
            
            return math.pow(2, exponent) == n