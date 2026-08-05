class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        inDegree = [0] * n
        suspicious = [False] * n

        for edge in invocations:
            u, v = edge[0], edge[1]
            adj[u].append(v)
            inDegree[v] += 1

        que = deque([k])
        suspicious[k] = True

        while que:
            curr = que.popleft()

            for ngbr in adj[curr]:
                inDegree[ngbr] -= 1
                if not suspicious[ngbr]:
                    que.append(ngbr)
                    suspicious[ngbr] = True

        result = []
        cannotRemove = False
        
        for i in range(n):
            if suspicious[i] and inDegree[i] > 0:
                cannotRemove = True
                break

            if not suspicious[i]:
                result.append(i)

        if cannotRemove:
            return list(range(n))
        
        return result
        