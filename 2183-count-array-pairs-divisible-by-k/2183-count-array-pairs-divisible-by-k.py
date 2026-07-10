class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for i in nums:
            temp = gcd(i, k)
            for j in freq:
                if (temp * j) % k == 0:
                    count += freq[j]
            if temp not in freq:
                freq[temp] = 0
            freq[temp] += 1

        return count