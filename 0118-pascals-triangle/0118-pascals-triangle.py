class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        if n==2:
            return [[1],[1,1]]
        a=[[1],[1,1]]
        for i in range(2,n):
            b=[]
            for j in range(i):
                if j==0:
                    b.append(1)
                else :
                    b.append(a[i-1][j]+a[i-1][j-1])
            b.append(1)
            a.append(b)
        return a
                
                



        