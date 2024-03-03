class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        a=list(d.values())
        x,y=0,0
        for j in a:
            x=x+j//2
            y=y+j%2
        return [x,y]
                