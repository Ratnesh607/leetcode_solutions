class Solution:
    def reverseByType(self, s: str) -> str:
        new_s = []
        special = []
        for i in s:
            if "a" <= i <= "z":
                new_s.append(i)
            else:
                special.append(i)


        ans = []
        j = len(new_s) - 1
        k = len(special) - 1
        for i in s:
            if "a" <= i <= "z":
                ans.append(new_s[j])
                j -= 1
            else:
                ans.append(special[k])
                k -= 1

        return "".join(ans)