from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x :x[1])
        higher = float('-inf')
        arrow = 0
        for point in points:
            if point[0] <= higher:
                continue
            else:
                arrow += 1
                higher = point[1]
        return arrow
            


