class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        ml=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                a=s[i:j+1]
                if a==a[::-1]:
                    if len(a)>ml:
                        r=a
                        ml=max(ml,len(a))
        return r
        

        