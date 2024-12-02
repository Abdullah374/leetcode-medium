from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n= len(isConnected)
        visited = [False] * n
        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        province_count = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                province_count += 1
        return province_count
