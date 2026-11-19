class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        small = [float('inf')] * 3
        large = [float('-inf')] * 3
        for i in nums:
            if i < small[0]:
                small = [i, small[0], small[1]]
            elif i < small[1]:
                small = [small[0], i, small[1]]
            elif i < small[2]:
                small[2] = i

            if i > large[0]:
                large = [i, large[0], large[1]]
            elif i > large[1]:
                large = [large[0], i, large[1]]
            elif i > large[2]:
                large[2] = i

        return min(large[0] - small[2], large[1] - small[1], large[2] - small[0])