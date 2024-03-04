class Solution:
    def countBalls(self, l: int, h: int) -> int:
        def su(n):
            s=0
            while n!=0:
                s=s+n%10
                n=n//10
            return s
        a=[]
        d={}
        for i in range(l,h+1):
            s=su(i)
            a.append(s)
            d[s]=d.get(s,0)+1
        return max(d.values())


        