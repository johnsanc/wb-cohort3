class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        length = len(nums)
        
        for _ in range(k):
            first = nums.pop(length-1)
            nums.insert(0, first)