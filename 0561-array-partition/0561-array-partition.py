class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        freq = [0] * 20001
        for num in nums:
            freq[num + 10000] += 1

        status = True
        ans = 0
        for i in range(20001):
            while freq[i]:
                if status:
                    ans += i - 10000
                status = not status
                freq[i] -= 1
        return ans