class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = []
        ans = []
        k = 0
        for i in nums:
            if i != -1:
                seen.append(i)
                k = 0
            else:
                k += 1
                if k <= len(seen):
                    ans.append(seen[-k])
                else:
                    ans.append(-1)
        return ans