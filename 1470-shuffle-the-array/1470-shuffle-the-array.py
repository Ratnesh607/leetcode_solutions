class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] * 1001 + nums[i + n]

        for i in range(n - 1, -1, -1):
            nums[2 * i + 1] = nums[i] % 1001
            nums[2 * i] = nums[i] // 1001

        return nums