class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        a=[]
        for i in moves:
            a.append(i)
        if moves.count("L")<moves.count("R"):
            b=moves.count("R")+moves.count("_")
            return b-moves.count("L")
        else :
            b=moves.count("L")+moves.count("_")
            return b-moves.count("R")
