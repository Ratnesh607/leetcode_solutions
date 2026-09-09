class Solution:
    def countCommas(self, n: int) -> int:
        countComma = 0
        curr_limit = 1000
        while n >= curr_limit:
            countComma += n - curr_limit + 1
            curr_limit *= 1000
        return countComma