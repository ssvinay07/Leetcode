class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        a=[[0]*n for x in range(m)]
        for i in range(len(indices)):
            for j in range(n):
                a[indices[i][0]][j]=a[indices[i][0]][j]+1
            for k in range(m):
                a[k][indices[i][1]]=a[k][indices[i][1]]+1
        count=0
        for y in range(m):
            for z in range(n):
                if a[y][z]%2==1:
                    count=count+1
        return count