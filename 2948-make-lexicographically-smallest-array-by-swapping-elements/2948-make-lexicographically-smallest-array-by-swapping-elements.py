class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted(nums)
        groups = []
        current = deque([arr[0]])
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] > limit:
                groups.append(current)
                current = deque()
            current.append(arr[i])
        groups.append(current)

        numToGroup = {}
        for group, values in enumerate(groups):
            for value in values:
                numToGroup[value] = group

        result = []
        for num in nums:
            group = numToGroup[num]
            result.append(groups[group].popleft())

        return result