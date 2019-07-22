class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output =[]
        last = len(nums2) - 1
        
        for n in nums1:
            index = nums2.index(n)
            
            if index == last:
                output.append(-1)
                
            else:
                for i in range(index + 1, last + 1):
                    if nums2[i] > nums2[index]:
                        output.append(nums2[i])
                        break
                    if i == last:
                        output.append(-1)
        return output