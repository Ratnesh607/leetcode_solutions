class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        Open = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                Open.append(i)
            elif Open and Open[-1] == "(" and  i == ")":
                Open.pop()
            elif Open and Open[-1] == "{" and  i == "}":
                Open.pop()
            elif Open and Open[-1] == "[" and  i == "]":
                Open.pop()
            else:
                return False
            
        return not Open