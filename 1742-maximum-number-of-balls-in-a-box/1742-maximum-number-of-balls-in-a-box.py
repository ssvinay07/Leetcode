class Solution:
    def countBalls(self, l: int, h: int) -> int:
        def su(n):
            s=0
            while n!=0:
                s=s+n%10
                n=n//10
            return s
        a=[]
        for i in range(l,h+1):
            a.append(su(i))
        d={}
        for z in a:
            d[z]=d.get(z,0)+1
        return max(d.values())


        