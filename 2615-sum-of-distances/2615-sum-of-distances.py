class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        index = {}
        for i in range(n):
            if nums[i] in index:
                prefix[i] = abs(index[nums[i]][0] - (i*index[nums[i]][1]))
                index[nums[i]][0] += i
                index[nums[i]][1] += 1
            else:
                index[nums[i]] = [i, 1]

        index.clear()
        for i in range(n - 1, -1, -1):
            if nums[i] in index:
                prefix[i] += abs(index[nums[i]][0] - (i * index[nums[i]][1]))
                index[nums[i]][0] += i
                index[nums[i]][1] += 1
            else:
                index[nums[i]] = [i, 1]

        return prefix       