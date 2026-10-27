class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        temp = image[sr][sc]
        if temp == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()
            for i in directions:
                nr = r + i[0]
                nc = c + i[1]
                if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == temp:
                    image[nr][nc] = color
                    queue.append((nr,nc))

        return image