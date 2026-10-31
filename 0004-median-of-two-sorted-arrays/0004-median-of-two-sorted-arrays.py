class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        med=sorted(nums1+nums2)
        arr=len(med)        
        if arr % 2 ==1:
            return med[arr//2]
        else:
            return (med[(arr // 2) - 1] + med[arr // 2]) / 2.0