class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            d[i]=d.get(i,0)+1
        a=list(d.values())
        l1=len(a)
        a=set(a)
        l2=len(a)
        return True if l1==l2 else False
        