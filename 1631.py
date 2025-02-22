from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        q = [(0,0,0)]
        m = len(heights)
        n = len(heights[0])
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0

        while q:
            effort, i,j = heappop(q)

            if i == m-1 and j == n-1:
                    return effort
            for sr,sc in directions:
                nr, nc = i+sr, j+sc
                
                if 0 <=nr<m and 0<=nc<n:
                    new_effort = max(effort,abs(heights[i][j]-heights[nr][nc]))
                    if new_effort < dist[nr][nc]:
                        heappush(q,(new_effort, nr,nc))
                        dist[nr][nc] = new_effort
                   
        return dist[m-1][n-1]


