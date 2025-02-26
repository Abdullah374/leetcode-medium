import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = {i:{} for i in range(n)}
        mod = 10**9 + 7

        for u,v, time in roads:
            graph[u][v] = time
            graph[v][u] = time

        short_time = {i: float('inf') for i in range(n)}
        short_time[0] = 0
        q = [(0,0)]
        ways = {i: 0 for i in range(n)}
        ways[0] = 1

        while q:
            current_time, node = heapq.heappop(q)

            for neighbor, time in graph[node].items():
                new_time = time + current_time
                if new_time < short_time[neighbor]:
                    short_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(q,(new_time, neighbor))
                elif new_time == short_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod


        
        return ways[n-1]


