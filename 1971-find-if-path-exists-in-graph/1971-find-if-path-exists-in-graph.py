class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True 
        arr = [[] for _ in range(n)]
        for i in edges:
            arr[i[0]].append(i[1])
            arr[i[1]].append(i[0])

        queue = deque([source])
        visited = [False]*n
        visited[source] = True
        while queue:
            node = queue.popleft()
            for i in arr[node]:
                if visited[i] == False:
                    if i == destination:
                        return True
                    visited[i] = True
                    queue.append(i)

        return False
                