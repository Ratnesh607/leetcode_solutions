class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        freq = [0]*1001
        for i in range(len(nums)):
            for j in nums[i]:
                freq[j] += 1
        
        ans = []
        for i in range(1001):
            if freq[i] == len(nums):
                ans.append(i)
        return ans