class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = [0] * 37
        for i in range(1, n + 1):
            num = i
            total = 0
            while num:
                total += num % 10
                num //= 10
            freq[total] += 1
        maxCount = max(freq)
        count = 0
        for i in freq:
            if i == maxCount:
                count += 1
        return count