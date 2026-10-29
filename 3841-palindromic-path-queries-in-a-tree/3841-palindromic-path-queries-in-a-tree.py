class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        s = list(s)
        tin = [0] * n
        tout = [0] * n
        depth = [0] * n
        parent = [-1] * n
        eulerTour = [0] * (2 * n)
        time = 0
        stack = [(0, -1, 0)]
        while stack:
            node, par, state = stack.pop()
            if state == 0:
                parent[node] = par
                tin[node] = time
                eulerTour[time] = 1 << (ord(s[node]) - ord('a'))
                time += 1
                stack.append((node, par, 1))

                for child in reversed(adj[node]):
                    if child != par:
                        depth[child] = depth[node] + 1
                        stack.append((child, node, 0))
            else:
                tout[node] = time
                eulerTour[time] = 1 << (ord(s[node]) - ord('a'))
                time += 1

        cols = n.bit_length()
        ancestorTable = [[-1] * cols for _ in range(n)]
        for node in range(n):
            ancestorTable[node][0] = parent[node]

        for j in range(1, cols):
            for node in range(n):
                prev = ancestorTable[node][j - 1]
                if prev != -1:
                    ancestorTable[node][j] = ancestorTable[prev][j - 1]

        N = 2 * n
        size = 1
        while size < N:
            size *= 2

        segmentTree = [0] * (2 * size)
        for i in range(N):
            segmentTree[size + i] = eulerTour[i]

        for i in range(size - 1, 0, -1):
            segmentTree[i] = segmentTree[2 * i] ^ segmentTree[2 * i + 1]

        def updateSegTree(index, val):
            index += size
            segmentTree[index] = val
            index //= 2
            while index:
                segmentTree[index] = segmentTree[2 * index] ^ segmentTree[2 * index + 1]
                index //= 2

        def querySegmentTree(start, end):
            start += size
            end += size
            mask = 0
            while start < end:
                if start % 2:
                    mask ^= segmentTree[start]
                    start += 1

                if end % 2:
                    end -= 1
                    mask ^= segmentTree[end]

                start //= 2
                end //= 2

            return mask

        def getLCA(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            j = 0
            while diff:
                if diff & 1:
                    u = ancestorTable[u][j]

                diff >>= 1
                j += 1

            if u == v:
                return u

            for j in range(cols - 1, -1, -1):
                if ancestorTable[u][j] != ancestorTable[v][j]:
                    u = ancestorTable[u][j]
                    v = ancestorTable[v][j]

            return ancestorTable[u][0]

        result = []
        for q in queries:
            parts = q.split()
            typ = parts[0]
            if typ == "update":
                node = int(parts[1])
                c = parts[2]
                s[node] = c
                charValue = 1 << (ord(c) - ord('a'))
                updateSegTree(tin[node], charValue)
                updateSegTree(tout[node], charValue)

            else:
                u = int(parts[1])
                v = int(parts[2])
                lcaNode = getLCA(u, v)
                charValue = 1 << (ord(s[lcaNode]) - ord('a'))
                mask = ( querySegmentTree(0, tin[u] + 1) ^ querySegmentTree(0, tin[v] + 1) ^ charValue )
                result.append((mask & (mask - 1)) == 0)

        return result