class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            grp = []
            for i in range(0, len(s), k):
                temp = s[i:i+k]
                total = 0
                for j in temp:
                    total += int(j)

                grp.append(str(total))

            s = "".join(grp)

        return s
