class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        a=[]
        for j in d:
            a.append([d.get(j),j])
        a.sort(reverse=True)
        r=""
        for k in a:
            for x in range(k[0]):
                r=r+k[1]
        return r