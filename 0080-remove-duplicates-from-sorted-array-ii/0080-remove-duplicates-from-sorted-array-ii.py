class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        count=0
        for i in nums:
            if nums.count(i)>2 and i!=" ":
                a=nums.count(i)
                for j in range(a-2):
                    nums.remove(i)
                    nums.append(" ")
                    count=count+1
        return l-count

        