class Solution:
    def checkString(self, s: str) -> bool:
        A = False
        for i in s:
            if i == "a" and A:
                return False
            if i == "b":
                A = True
        return True
        