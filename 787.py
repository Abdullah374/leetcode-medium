import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:{} for i in range(n)}
        for u,v,cost in flights:
            graph[u][v] = cost

        min_cost = {i:{} for i in range(n)}
        min_cost[src][0] = 0
        q = [(0,src,0)]
        

        while q:
            current_cost, current_node , stop = heapq.heappop(q)
            if current_node == dst:
                return current_cost

            if stop > k:
                continue
            for neighbor,price in graph[current_node].items():
                new_cost = current_cost + price
                new_stop = stop + 1
                
                if new_stop not in min_cost[neighbor] or new_cost < min_cost[neighbor][new_stop]:
                    min_cost[neighbor][new_stop] = new_cost
                    heapq.heappush(q,(new_cost, neighbor, new_stop))
        
        return -1