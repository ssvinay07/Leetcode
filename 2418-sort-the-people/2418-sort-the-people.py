class Solution:
    def sortPeople(self, names: List[str], h: List[int]) -> List[str]:
        d={}
        for i in range(len(names)):
            d[h[i]]=names[i]
        a=list(d.keys())
        a.sort(reverse=True)
        b=[]
        for j in a:
            b.append(d[j])
        return b

        