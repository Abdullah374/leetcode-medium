from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = deque()
        fresh_count = 0

        for i,row in enumerate(grid):
            for j,number in enumerate(row):
                if number == 2:
                    queue.append((i,j,0))
                elif number == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0
        max_time = 0

        while queue:
            r,c, time = queue.popleft()

            for dr, dc in directions:
                nr , nc = r +dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                   
                    queue.append((nr,nc, time+1))
                    max_time = max(max_time, time+1)

        return max_time if fresh_count == 0 else -1
        
        