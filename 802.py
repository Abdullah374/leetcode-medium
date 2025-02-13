from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rec = set()
        visited = set()
        result = []


        def dfs(node):
            if node in rec:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            rec.add(node)

            
            for neighbor in graph[node]:
                if dfs(neighbor):
                    return True
            result.append(node)
            rec.remove(node)
            return False

        
        for node in range(len(graph)):
            dfs(node)
        return sorted(result)



            