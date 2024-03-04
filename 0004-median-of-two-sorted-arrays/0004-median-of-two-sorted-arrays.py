class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a=list(nums1+nums2)
        a.sort()
        if len(a)%2==1:
            return a[len(a)//2]
        else :
            return (a[len(a)//2]+a[(len(a)//2)-1])/2
        