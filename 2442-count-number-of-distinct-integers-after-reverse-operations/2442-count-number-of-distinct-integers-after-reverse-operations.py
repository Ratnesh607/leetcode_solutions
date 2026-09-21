class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        uniqueVal = set()
        for i in nums:
            num = i
            revnum = 0
            while num:
                revnum *= 10
                revnum += num % 10
                num //= 10
            uniqueVal.add(i)
            uniqueVal.add(revnum)
        return len(uniqueVal)