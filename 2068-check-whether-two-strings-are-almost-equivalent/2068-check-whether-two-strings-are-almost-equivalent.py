class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d1={}
        for i in word1:
            d1[i]=d1.get(i,0)+1
        d2={}
        for j in word2:
            d2[j]=d2.get(j,0)+1
        w=list(word1+word2)
        for k in w:
            a=d1.get(k,0)
            b=d2.get(k,0)
            if abs(a-b)>3:
                return False
        return True

