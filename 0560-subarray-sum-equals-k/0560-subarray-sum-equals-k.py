class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Dict = {0: 1}
        total = 0
        count = 0

        for i in nums:
            total += i
            if total - k in Dict:
                count += Dict[total - k]

            Dict[total] = Dict.get(total, 0) + 1

        return count           