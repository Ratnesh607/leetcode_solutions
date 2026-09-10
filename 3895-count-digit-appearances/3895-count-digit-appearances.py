class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for i in nums:
            temp = i
            while temp:
                if temp % 10 == digit:
                    count += 1
                temp //= 10
        return count
        