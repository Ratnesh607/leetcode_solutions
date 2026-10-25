class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        count = set()
        num = -1
        for i in word:
            if "0" <= i <= "9":
                if num == -1:
                    num = 0
                num *= 10
                num += int(i)
            elif num != -1:
                count.add(num)
                num = -1
        if num != -1:
            count.add(num)

        return len(count)
        