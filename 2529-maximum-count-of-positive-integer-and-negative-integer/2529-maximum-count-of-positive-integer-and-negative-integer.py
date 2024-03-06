class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0
        for i in nums:
            if i<0:
                neg=neg+1
            else :
                break
        pos=len(nums)-neg-nums.count(0)
        return max(pos,neg)
        