class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=len(nums1)
        b=len(nums2)
        flag=0
        r=[]
        for i in range(a):
            c=nums2.index(nums1[i])
            flag=0
            for j in range(c+1,b):
                if nums2[c]<nums2[j]:
                    r.append(nums2[j])
                    flag=1
                    break
            if flag==0:
                r.append(-1)
        return r


        