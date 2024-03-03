class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mip=p[0]
        mp=0
        for i in p[1:]:
            mp=max(mp,i-mip)
            mip=min(mip,i)
        return mp