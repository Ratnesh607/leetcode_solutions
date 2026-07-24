class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        maxNum = max(nums)

        T = 1
        while T <= maxNum:
            T *= 2

        xorPairs = [False]*T
        xorTriplets = [False]*T

        for i in range(n):
            for j in range(i, n):
                xorPairs[nums[i] ^ nums[j]] = True

        count = 0
        for i in range(T):
            if xorPairs[i]:
                for j in nums:
                    temp = i ^ j
                    if xorTriplets[temp] == False:
                        count += 1
                    xorTriplets[temp] = True

        return count
        