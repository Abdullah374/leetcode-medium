
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = {}
        visited = set()
        change = 0

        for a,b in connections:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append((b,1))
            graph[b].append((a,0))
        
        def dfs(city):
            nonlocal change
            visited.add(city)
            for neighbor, original in graph[city]:
                if neighbor not in visited:
                    change += original
                    dfs(neighbor)
        dfs(0)
        return change