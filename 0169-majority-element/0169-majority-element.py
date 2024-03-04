class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in list(set(nums)):
            if nums.count(i)>len(nums)/2:
                return i
                break
        