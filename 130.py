from typing import List
from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])
        q = deque()

        def mark(i,j):
            if 0<=i<m and 0<=j<n and board[i][j] == "O":
                board[i][j] = "T"
                q.append((i,j))

        for i in range(m):
            mark(i,0)
            mark(0,n-1)

        for i in range(n):
            mark(0,i)
            mark(m-1, i)

        while q:
            i, j = q.popleft()
            for sr, sc in [(1,0),(-1,0), (0,1), (0,-1)]:
                nr,nc = i+sr, j+sc
                mark(nr, nc)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] == "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] == "O"