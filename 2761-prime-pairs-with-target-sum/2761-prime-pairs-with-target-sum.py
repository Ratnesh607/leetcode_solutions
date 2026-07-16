class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        arr = [True]*n           
        for i in range(2,n):
            if arr[i]:
                for j in range(i+i,n,i):
                    arr[j] = False

        i = 2
        j = n - 1
        ans = []
        while i <= j:
            if not arr[i]:
                i += 1
                continue

            if not arr[j]:
                j -= 1
                continue

            if i + j == n:
                ans.append([i, j])
                i += 1
                j -= 1
            elif i + j > n:
                j -= 1
            else:
                i += 1

        return ans