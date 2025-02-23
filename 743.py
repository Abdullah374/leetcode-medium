import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        graph = {i:{} for i in range (1,n+1)}

        for u,v, time in times:
            graph[u][v] = time

        short_time = {i:float('inf') for i in range(1,n+1) }
        q = [(0,k)]
        short_time[k] = 0

        
        while q:
            current_time, node = heapq.heappop(q)
            
            for neighbor, time in graph[node].items():
                new_time = time + current_time
                if new_time < short_time[neighbor]:
                    short_time[neighbor] = new_time
                    heapq.heappush(q,(new_time, neighbor))
        if any(node != k and short_time[node] == float('inf') for node in range(1, n+1)):
            return -1
        return max(short_time.values())

