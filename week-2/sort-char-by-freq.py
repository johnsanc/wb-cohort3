from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        result = ""
        
        for char,freq in count.most_common():
            result += char * freq

        return result