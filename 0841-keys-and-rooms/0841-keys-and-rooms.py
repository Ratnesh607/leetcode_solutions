class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        queue = deque([0])
        key = [False]*n
        key[0] = True
        while queue:
            node = queue.popleft()            
            for i in rooms[node]:
                if not key[i]:
                    key[i] = True
                    queue.append(i)

        for i in key:
            if not i:
                return False
        return True 
        