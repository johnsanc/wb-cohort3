class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = set()
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        
        if nums1_len < nums2_len:
            for num in nums1:
                if num in nums2:
                    intersection.add(num)
        else:
            for num in nums2:
                if num in nums1:
                    intersection.add(num)
                    
        return list(intersection)