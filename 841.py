from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set()
        keys.add(0)
        stack = [0]

        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in keys:
                    keys.add(key)
                    stack.append(key)

        return len(keys) == len(rooms)