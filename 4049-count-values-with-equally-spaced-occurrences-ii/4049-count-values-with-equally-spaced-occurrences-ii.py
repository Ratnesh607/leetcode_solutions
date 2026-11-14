class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = [i]
            else:
                freq[nums[i]].append(i)

        count = 0
        for i in freq:
            flag = True
            if len(freq[i]) >= 3:
                for idx in range(1, len(freq[i]) - 1):
                    if freq[i][idx] - freq[i][idx - 1] != freq[i][idx + 1] - freq[i][idx]:
                        flag = False
                        break

                if flag:
                    count += 1
        return count