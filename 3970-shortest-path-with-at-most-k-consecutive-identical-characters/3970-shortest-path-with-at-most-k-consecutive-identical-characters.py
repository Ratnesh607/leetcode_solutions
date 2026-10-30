class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for i in edges:
            adj[i[0]].append((i[1], i[2]))

        if n == 1:
            return 0

        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        while pq:
            cost, node, consec = heapq.heappop(pq)
            if cost != dist[node][consec]:
                continue

            if node == n - 1:
                return cost

            for nbr, wt in adj[node]:
                if labels[node] == labels[nbr]:
                    newConsec = consec + 1
                else:
                    newConsec = 1

                if newConsec > k:
                    continue

                newCost = cost + wt
                if newCost < dist[nbr][newConsec]:
                    dist[nbr][newConsec] = newCost
                    heapq.heappush(pq, (newCost, nbr, newConsec))

        return -1