class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        freq = {}
        ans = float("inf")
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = []
            freq[nums[i]].append(i)
            if len(freq[nums[i]]) >= 3:
                distance = abs(freq[nums[i]][-1] - freq[nums[i]][-2]) + abs(freq[nums[i]][-1] - freq[nums[i]][-3]) + abs(freq[nums[i]][-3] - freq[nums[i]][-2])
                ans = min(ans, distance)
                
        return ans if ans != float("inf") else -1
        