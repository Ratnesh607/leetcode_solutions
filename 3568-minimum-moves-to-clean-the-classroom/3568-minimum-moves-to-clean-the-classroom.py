class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        litterBit = [[-1] * n for _ in range(m)]
        litterCount = 0
        startRow = 0
        startCol = 0
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    startRow = r
                    startCol = c
                elif classroom[r][c] == 'L':
                    litterBit[r][c] = litterCount
                    litterCount += 1

        if litterCount == 0:
            return 0

        allCollected = (1 << litterCount) - 1
        queue = [(startRow, startCol, energy, 0)]
        seen = set()
        seen.add((startRow, startCol, energy, 0))
        moves = 0
        front = 0
        while front < len(queue):
            size = len(queue) - front
            for _ in range(size):
                row, col, energyLeft, mask = queue[front]
                front += 1
                if mask == allCollected:
                    return moves
                if energyLeft == 0:
                    continue

                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    if classroom[nr][nc] == 'X':
                        continue

                    nextEnergy = energyLeft - 1
                    nextMask = mask
                    if classroom[nr][nc] == 'R':
                        nextEnergy = energy
                    elif classroom[nr][nc] == 'L':
                        nextMask |= (1 << litterBit[nr][nc])
                        
                    state = (nr, nc, nextEnergy, nextMask)
                    if state not in seen:
                        seen.add(state)
                        queue.append(state)
            moves += 1
        return -1