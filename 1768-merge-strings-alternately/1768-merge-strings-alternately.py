class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=len(word1)
        b=len(word2)
        m=""
        for i in range(max(a,b)):
            if i<len(word1):m=m+word1[i]
            if i<len(word2):m=m+word2[i]
        return m
        

        