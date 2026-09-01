class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        check = [False]*(k + 1)
        count = 0
        temp = k
        for i in range(len(nums) - 1, -1, -1):
            count += 1
            if nums[i] <= k and check[nums[i]] == False:
                check[nums[i]] = True
                temp -= 1
                if temp == 0:
                    return count