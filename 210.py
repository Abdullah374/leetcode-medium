from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return list(range(numCourses))

        visited = set()
        rec = set()
        result = []

        graph = {i: [] for i in range(numCourses)}

        for dst, src in prerequisites:
            graph[src].append(dst)

        def dfs(node):
            if node in rec:
                return True
            if node in visited:
                return False
            visited.add(node)
            rec.add(node)

            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True

            rec.remove(node)
            result.append(node)
            return False
        
        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return []
        return result[::-1]