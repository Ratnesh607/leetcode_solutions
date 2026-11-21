class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = [0]*10
        while n:
            freq[n % 10] += 1
            n //= 10

        ans = 0
        for i in range(10):
            ans += freq[i] * i

        return ans