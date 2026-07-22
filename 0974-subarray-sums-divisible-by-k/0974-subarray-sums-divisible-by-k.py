class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        Dict = {0: 1}
        total = 0
        count = 0

        for i in nums:
            total += i
            rem = total % k
            count += Dict.get(rem, 0)
            Dict[rem] = Dict.get(rem, 0) + 1

        return count