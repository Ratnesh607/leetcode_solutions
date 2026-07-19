class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        numindex = []
        for i in range(len(nums)):
            numindex.append([nums[i], i])

        numindex.sort(reverse = True)
        largest = numindex[:k]
        largest.sort(key=lambda x: x[1])

        return [i[0] for i in largest]