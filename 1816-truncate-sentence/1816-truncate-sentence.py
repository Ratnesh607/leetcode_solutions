class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        temp = 0
        for i in range(len(s)):
            if s[i] == " ":
                temp = i
                k -= 1
                if k == 0:
                    return s[0:temp]
        return s