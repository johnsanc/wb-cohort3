class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        results = []
        for n in range(left, right + 1):
            if self.divisibleBy(n):
                results.append(n)
        return results
        
    def divisibleBy(self, n):
        if n == 0:
            return False
        for l in str(n):
            if int(l) == 0:
                return False
            elif n % int(l) > 0:
                return False
        return True