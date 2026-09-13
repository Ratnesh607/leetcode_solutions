class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        points1 = []
        points2 = []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    points1.append((i, j))

                if img2[i][j] == 1:
                    points2.append((i, j))

        freq = {}
        ans = 0
        for i in points1:
            for j in points2:
                dx = j[0] - i[0]
                dy = j[1] - i[1]
                freq[(dx, dy)] = freq.get((dx, dy), 0) + 1
                ans = max(ans, freq[(dx, dy)])
        return ans