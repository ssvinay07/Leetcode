class Solution:
    def minimumSum(self, num: int) -> int:
        a=[]
        for i in str(num):
            a.append(int(i))
        a.sort(reverse=True)
        return a[0]+a[1]+a[2]*10+a[3]*10

        
        
        