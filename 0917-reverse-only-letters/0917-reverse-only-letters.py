class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        new_s = []
        for i in s:
            if "a" <= i <= "z" or "A" <= i <= "Z":
                new_s.append(i)

        ans = []
        j = len(new_s) - 1
        for i in s:
            if "a" <= i <= "z" or "A" <= i <= "Z":
                ans.append(new_s[j])
                j -= 1
            else:
                ans.append(i)

        return "".join(ans)