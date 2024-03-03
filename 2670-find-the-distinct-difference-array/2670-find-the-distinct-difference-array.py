class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        diff=[]
        for i in range(len(nums)):
            l=len(set(nums[0:i+1]))-len(set(nums[i+1:]))
            diff.append(l)
        return diff