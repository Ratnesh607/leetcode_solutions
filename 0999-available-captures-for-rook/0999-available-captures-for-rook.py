class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        idx = ()
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    idx = (i , j)
                    break

            if idx:
                break

        pawns = 0
        for i in range(idx[1] - 1, -1, -1):
            if board[idx[0]][i] == "B":
                break
            elif board[idx[0]][i] == "p":
                pawns += 1
                break

        for i in range(idx[1] + 1, 8):
            if board[idx[0]][i] == "B":
                break
            elif board[idx[0]][i] == "p":
                pawns += 1
                break

        for i in range(idx[0] - 1, -1, -1):
            if board[i][idx[1]] == "B":
                break
            elif board[i][idx[1]] == "p":
                pawns += 1
                break

        for i in range(idx[0] + 1, 8):
            if board[i][idx[1]] == "B":
                break
            elif board[i][idx[1]] == "p":
                pawns += 1
                break

        return pawns