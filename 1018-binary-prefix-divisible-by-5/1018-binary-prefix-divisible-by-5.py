class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        deci = 0
        for bit in nums:
            deci = ((deci << 1) + bit) % 5
            ans.append(deci == 0)
        return ans        