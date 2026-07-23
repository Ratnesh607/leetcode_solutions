class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        freq = {}
        dist = 0
        for i in range(n):
            if nums[i] not in freq:
                dist += 1
            prefix[i] = dist
            freq[nums[i]] = freq.get(nums[i],0) + 1
        freq.clear()
        dist = 0
        for i in range(n-1, -1, -1):
            prefix[i] -= dist
            if nums[i] not in freq:
                dist += 1
                freq[nums[i]] = 0
    
        return prefix


            
        