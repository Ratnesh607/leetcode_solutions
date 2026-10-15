class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i]:
                i += 1
                temp = k
                while temp and i < n:
                    if nums[i]:
                        return False
                    i += 1
                    temp -= 1
            else:
                i += 1
        return True