class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = []
        total = 0
        k = k1 + k2
        for i in range(len(nums1)):
            temp = abs(nums1[i] - nums2[i])
            diff.append(temp)
            total += temp
        if total <= k:
            return 0

        l = 0
        r = max(diff)
        while l < r:
            mid = (l + r) // 2
            count = 0
            for i in diff:
                if i > mid:
                    count += i - mid

            if count <= k:
                r = mid
            else:
                l = mid + 1

        ans = 0
        count = 0
        for i in diff:
            if i > l:
                count += i - l
                ans += l * l
            else:
                ans += i * i
        remaining = k - count
        if remaining > 0:
            ans -= remaining * (2 * l - 1)

        return ans