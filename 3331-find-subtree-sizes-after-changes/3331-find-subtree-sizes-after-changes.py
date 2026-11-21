class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        adj = [[] for _ in range(n)]
        for i in range(1, n):
            adj[parent[i]].append(i)

        ans = [1] * n
        prev = [-1] * n
        last = {}
        stack = [0]
        while stack:
            node = stack.pop()
            if node >= 0:
                prev[node] = last.get(s[node], -1)
                last[s[node]] = node
                stack.append(~node)

                for child in adj[node]:
                    stack.append(child)

            else:
                node = ~node
                last[s[node]] = prev[node]
                p = prev[node]
                if p == -1:
                    p = parent[node]

                if p != -1:
                    ans[p] += ans[node]

        return ans
        