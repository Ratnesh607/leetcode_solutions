class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        available = []
        busy = []
        for i in range(len(servers)):
            heapq.heappush(available, (servers[i], i))

        ans = []
        curr_time = 0
        for i in range(len(tasks)):
            curr_time = max(curr_time, i)
            while busy and busy[0][0] <= curr_time:
                time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            if not available:
                curr_time = busy[0][0]
                while busy and busy[0][0] <= curr_time:
                    time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            weight, idx = heapq.heappop(available)
            ans.append(idx)
            heapq.heappush(busy, (curr_time + tasks[i], weight, idx))


        return ans