from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        
        directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque([(0,0,1)])
        grid[0][0] = 1
    
        while q:
            i,j, length = q.popleft()
            
            if i == n-1 and j== n-1:
                return length

            for di, dj in directions:
                nr, nc = i+di, j+dj
                if 0<=nr<n and 0<=nc<n and grid[nr][nc]==0:

                    grid[nr][nc] = 1
                    q.append((nr, nc, length + 1))

        return -1

                


