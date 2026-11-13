class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = []
            freq[nums[i]].append(i)

        count = 0
        for i in freq:
            if len(freq[i]) == 3 and freq[i][1] - freq[i][0] == freq[i][2] - freq[i][1]:
                count += 1

        return count