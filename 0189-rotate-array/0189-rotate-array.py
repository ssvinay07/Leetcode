class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=len(nums)
        if l==1:
            nums=nums
        elif l==2:
            for i in range(k):
                nums.reverse()
        else :
            nums.extend(nums[0:l-k])
            for i in range(len(nums)-l):
                del nums[0]