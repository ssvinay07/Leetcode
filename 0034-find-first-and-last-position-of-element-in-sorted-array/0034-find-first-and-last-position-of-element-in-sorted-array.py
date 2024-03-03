class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a=[]
        if target in nums:
            a.append(nums.index(target))
            if nums.count(target)>1:
                nums.reverse()
                a.append(len(nums)-nums.index(target)-1)
            else :
                a.append(nums.index(target))
            return a

        else :
            return [-1,-1]


        