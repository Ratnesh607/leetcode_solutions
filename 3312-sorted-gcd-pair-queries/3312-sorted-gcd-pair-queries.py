class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        maxNum = max(nums)

        freq = [0] * (maxNum + 1)

        for num in nums:
            freq[num] += 1

        divFreq = [0] * (maxNum + 1)

        for d in range(1, maxNum + 1):
            for multiple in range(d, maxNum + 1, d):
                divFreq[d] += freq[multiple]

        gcdPairs = [0] * (maxNum + 1)

        for i in range(maxNum, 0, -1):
            count = divFreq[i]
            gcdPairs[i] = count * (count - 1) // 2

            for j in range(2 * i, maxNum + 1, i):
                gcdPairs[i] -= gcdPairs[j]

        prefixCountGcd = [0] * (maxNum + 1)

        for i in range(1, maxNum + 1):
            prefixCountGcd[i] = prefixCountGcd[i - 1] + gcdPairs[i]

        result = []

        for idx in queries:
            l = 1
            r = maxNum
            ans = 1

            while l <= r:
                mid = (l + r) // 2

                if prefixCountGcd[mid] > idx:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1

            result.append(ans)

        return result