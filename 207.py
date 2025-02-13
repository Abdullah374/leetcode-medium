from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = {}
        stack = []

        for i in range(numCourses):
            graph[i] = []

        for dst, src in prerequisites:
            graph[src].append(dst)

        rec_stack = set()

        def dfs(node):
            if node in rec_stack:
                return True
            if node in visited:
                return False
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True

              
            rec_stack.remove(node)
            return False

        for i in range(numCourses):
            if i not in visited:
                if dfs(i):
                    return False

        return True