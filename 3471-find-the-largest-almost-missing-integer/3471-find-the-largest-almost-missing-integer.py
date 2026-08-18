class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i , 0) + 1

        if k == 1:
            ans = -1
            for i in nums:
                if freq[i] == 1:
                    ans = max(ans, i)
            return ans

        if k == len(nums):
            return max(nums)
        
        if freq[nums[0]] == 1 and freq[nums[-1]] == 1:
            return max(nums[0], nums[-1])
        if freq[nums[0]] == 1:
            return nums[0]
        if freq[nums[-1]] == 1:
            return nums[-1]

        return -1