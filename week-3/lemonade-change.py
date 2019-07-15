from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        cost = 5
        
        for bill in bills:
            target_change = bill - cost
            # print("Target change to give: {}".format(target_change))
            change[bill] += 1
            if target_change > 0:
                while target_change >= 10 and change[10] > 0:
                    target_change -= 10
                    change[10] -= 1
                    # print("$10 bills left: ", change[10])
                while target_change % 5 == 0 and change[5] > 0 and target_change > 0:
                    target_change -= 5
                    change[5] -= 1
                    # print("$5 bills left: ", change[5])
                # print("Target change after change given: ", target_change)
                if target_change > 0:    
                    return False
        
        return True