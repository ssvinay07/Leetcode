class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a in b and b in a:
            return -1
        else :
            return max(len(a),len(b))
        

        