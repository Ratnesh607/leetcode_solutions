class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(31):
            count = 0
            for j in nums:
                if (j >> i) & 1:
                    count += 1

            if count >= k:
                ans |= (1 << i)
        return ans
        