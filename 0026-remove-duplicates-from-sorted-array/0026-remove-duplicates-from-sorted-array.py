class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expectedNums=[]
        for i in range(len(nums)):
            if nums[i] not in nums[0:i]:
                expectedNums.append(nums[i])
        for k in range(len(nums)-len(expectedNums)):
            nums.pop()
        for j in range (len(expectedNums)):
            nums[j]=expectedNums[j]


        