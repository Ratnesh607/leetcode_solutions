class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        check = {}
        count = 0
        for i in nums:
            if i > k:
                continue
            if k - i in check:
                count += 1
                check[k - i] -= 1
                if not check[k - i]:
                    del check[k - i]
            else:
                check[i] = check.get(i, 0) + 1
                
        return count