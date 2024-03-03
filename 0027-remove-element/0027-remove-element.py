class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=nums.count(val)
        for j in range(i):
            nums.remove(val)
        

        