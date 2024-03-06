class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        a=nums[0].copy()
        for i in nums[0]:
            for j in nums:
                if i not in j:
                    a.remove(i)
                    break
        a.sort()
        return a
            
        