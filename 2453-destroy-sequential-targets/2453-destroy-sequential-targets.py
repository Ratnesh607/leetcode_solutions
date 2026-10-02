class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        rem = {0: 0}
        ans = float("inf")
        for i in nums:
            rem[i % space] = rem.get(i % space, 0) + 1

        maxRem = 0
        for i in rem:
            if rem[maxRem] < rem[i]:
                maxRem = i
                
        Set = set()
        Set.add(maxRem)
        for i in rem:
            if rem[maxRem] == rem[i]:
                Set.add(i)

        for i in nums:
            if i % space in Set:
                ans = min(ans, i)

        return ans
