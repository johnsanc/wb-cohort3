class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = list(p)
        target.sort()
        target_length = len(target)
        char_list = list(s)
        indeces = []
        
        for i in range(0, len(char_list)):
            temp = char_list[i:i + target_length]
            temp.sort()
            if temp == target:
                indeces.append(i)
                
        return indeces

# This solution uses sorting, but too slow to pass 
# large test cases.  Only being shown as example