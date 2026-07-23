class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 2:
            return len(nums)

        ans = 2
        while ans <= n:
            ans *= 2
        return ans

        # return 1 << n.bit_length() <-- this is also correct appraoch to solve this problem


        