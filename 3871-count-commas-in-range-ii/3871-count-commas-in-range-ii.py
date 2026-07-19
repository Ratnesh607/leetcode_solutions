class Solution:
    def countCommas(self, n: int) -> int:
        comma = 0
        curr_limit = 1000
        while n >= curr_limit:
            comma += n - curr_limit + 1
            curr_limit *= 1000
        return comma