class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        depth = [0] * n
        depth[0] = 1
        q = deque([0])
        height = 1
        while q:
            node = q.popleft()
            for child in adj[node]:
                depth[child] = depth[node] + 1
                height = max(height, depth[child])
                q.append(child)

        total_w = 0
        for i in range(n):
            total_w += nums[i] * (height - depth[i] + 1)

        return total_w
            
        