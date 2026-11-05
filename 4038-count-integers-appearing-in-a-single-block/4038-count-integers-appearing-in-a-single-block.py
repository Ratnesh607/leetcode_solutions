class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = {}
        count = 0
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in range(len(nums)):
            if nums[i] in freq:
                temp = i
                while temp < len(nums) and nums[i] == nums[temp]:
                    temp += 1
                    freq[nums[i]] -= 1
                if not freq[nums[i]]:
                    count += 1
                del freq[nums[i]]

        return count