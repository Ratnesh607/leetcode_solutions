class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        for i in nums:
            num = i
            temp = 0
            while num:
                temp += num % 10
                num //= 10
            arr.append((temp, i))

        sortedArr = sorted(arr)
        pos = {nums[i]: i for i in range(n)}
        visited = [False] * n
        ans = 0
        for i in range(n):
            if visited[i] or pos[sortedArr[i][1]] == i:
                continue
            count = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = pos[sortedArr[j][1]]
                count += 1
            ans += count - 1
        return ans