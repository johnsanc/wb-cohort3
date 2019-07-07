from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        count_a = defaultdict(int)
        count_b = defaultdict(int)
        wordlist_A = A.split()
        wordlist_B = B.split()
        
        for word in wordlist_A:
            count_a[word] += 1
        
        for word in wordlist_B:
            count_b[word] += 1
            
        # get the uncommon words
        unique_a = set()
        unique_b = set()
        for key,val in count_a.items():
            if val == 1:
                unique_a.add(key)
        
        for key,val in count_b.items():
            if val == 1:
                unique_b.add(key)
        
        
        uncommon_both = []
        for item in unique_a:
            if item not in wordlist_B:
                uncommon_both.append(item)
        for item in unique_b:
            if item not in wordlist_A:
                uncommon_both.append(item)
                
        return uncommon_both