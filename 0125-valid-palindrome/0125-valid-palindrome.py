class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=""
        n=["0",'1','2','3','4','5','6','7','8','9']
        for i in s:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122:
                r=r+i.lower()
            if i in n:
                r=r+i
        return True if r==r[::-1] else False
        