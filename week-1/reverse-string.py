class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length > 1:
            mid = length // 2
            if length % 2 == 0:
                start = 0
                end = length - 1
                while start <= mid - 1 and end >= mid:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
            else:
                start = 0
                end = length - 1
                while start < mid and end > mid:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1