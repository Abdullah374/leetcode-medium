from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        q = deque()

        
        def mark(i, j):
            if 0<=i<m and 0<=j<n and grid[i][j] == 1:
                grid[i][j] = -1
                q.append((i,j))

        for i in range(m):
            mark(0,i)
            mark(n-1,i)

        for i in range(n):
            mark(i,0)
            mark(i,m-1)

        while q:
            i,j = q.popleft()
            for sr, sc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dr, dc = i+sr, j+sc
                mark(dr, dc)
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += 1

        return result
            
        
