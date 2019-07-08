from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = "".join((c if c.isalpha() else " ") for c in paragraph).split()
        count = Counter()
        
        for w in words:
            count[w.lower()] += 1
        
        for item,val in count.most_common():
            if item not in banned and item.isalpha():
                return item