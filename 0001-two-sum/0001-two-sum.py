class Solution:
    def twoSum(self, nums: List[int], t: int) -> List[int]:
        l=len(nums)
        for i in range(l):
            b=t-nums[i]
            if b in nums and i!=nums.index(b):
                return [i,nums.index(b)]


        