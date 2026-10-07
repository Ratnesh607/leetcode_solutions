class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            count = 0
            for i in s:
                if i == "(":
                    count += 1
                elif i == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        Set = {s}
        while True:
            ans = []
            for i in Set:
                if isValid(i):
                    ans.append(i)
            if ans:
                return ans
            newSet = set()
            for i in Set:
                for j in range(len(i)):
                    if i[j] == "(" or i[j] == ")":
                        newSet.add(i[:j] + i[j + 1:])
            Set = newSet