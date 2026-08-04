class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        x = min(nums)
        y = max(nums)
        check = [False]*(y + 1)
        for i in nums:
            check[i] = True

        ans = []
        for i in range(x, y+1):
            if check[i] == False:
                ans.append(i)
    
        return ans      