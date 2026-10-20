class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        prefMax = [0] * (n + 1)
        suffMin = [float("inf")] * (n + 1)
        prefDrop = [0] * n
        for i in range(n):
            prefMax[i + 1] = max(prefMax[i], nums[i])

        for i in range(n - 1, -1, -1):
            suffMin[i] = min(nums[i], suffMin[i + 1])

        for i in range(1, n):
            prefDrop[i] = prefDrop[i - 1]
            if nums[i - 1] > nums[i]:
                prefDrop[i] += 1

        def check(k):
            for start in range(0, n, k):
                end = start + k - 1
                drops = prefDrop[end] - prefDrop[start]
                if nums[end] > nums[start]:
                    drops += 1

                if drops > 1 or prefMax[start] > suffMin[start]:
                    return False
            return True
        ans = 0
        i = 1
        while i <= n // i:
            if n % i == 0:
                if check(i):
                    ans += i

                other = n // i
                if other != i and check(other):
                    ans += other
            i += 1
        return ans