class Solution:
    def minimizedStringLength(self, s: str) -> int:
        a=[]
        for i in s:
            if i not in a:
                a.append(i)
        return len(a)
        