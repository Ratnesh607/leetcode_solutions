class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 0
        count_prev = 0
        prev = word[0]
        for i in word:
            if i == prev:
                count_prev += 1
            else:
                ans += count_prev
                prev = i
                count_prev = 0

        ans += count_prev

        return ans
             