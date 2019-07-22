import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heapq.heapify(nums)
        return heapq.nlargest(k, counts, key=lambda x: counts[x])
    