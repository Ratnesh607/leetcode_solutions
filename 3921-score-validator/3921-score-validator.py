class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        ans = [0, 0]
        for i in events:
            if "0" <= i <= "6":
                ans[0] += int(i)

            elif i == "WD" or i == "NB":
                ans[0] += 1

            elif i == "W":
                ans[1] += 1
                if ans[1] == 10:
                    break

        return ans
        