class Solution:
    def getRow(self, r: int) -> List[int]:
        a=[[1],[1,1]]
        for i in range(2,r+1):
            b=[]
            for j in range(i):
                if j==0:
                    b.append(1)
                else :
                    b.append(a[i-1][j]+a[i-1][j-1])
            b.append(1)
            a.append(b)
        return a[r]
        