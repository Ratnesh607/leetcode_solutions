class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prefix = [0]*n
        index = {}
        for i in range(n):
            if arr[i] in index:
                prefix[i] = abs(index[arr[i]][0] - (i*index[arr[i]][1]))
                index[arr[i]][0] += i
                index[arr[i]][1] += 1
            else:
                index[arr[i]] = [i, 1]

        index.clear()
        for i in range(n-1, -1, -1):
            if arr[i] in index:
                prefix[i] += abs(index[arr[i]][0] - (i*index[arr[i]][1]))
                index[arr[i]][0] += i
                index[arr[i]][1] += 1
            else:
                index[arr[i]] = [i, 1]

        return prefix