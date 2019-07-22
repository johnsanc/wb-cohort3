class Solution:
    def calPoints(self, ops: List[str]) -> int:
        valid = [0]
        total = 0
        
        for op in ops:
            if self.isNumber(op):
                total += int(op)
                valid.append(int(op))
            elif op.isalpha():
                if op == "C":
                    last = valid.pop()
                    total -= last
                else:
                    last = valid[-1]
                    total += last * 2
                    valid.append(last * 2)
            else:
                last1, last2 = valid[-1], valid[-2]
                total += last1 + last2
                valid.append(last1 + last2)
        
        return total
    
    def isNumber(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False
        