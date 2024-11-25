from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # pairs = 0
        # for row in grid:
        #     for j in range(len(grid)):
        #         col = [grid[i][j] for i in range(len(grid))]
        #         if row == col:
        #             pairs+=1
        # return pairs

        row_hash = {}

        for row in grid:
            row_tuple = tuple(row)
            row_hash[row_tuple] = row_hash.get(row_tuple, 0) + 1
        
        pairs = 0
        for j in range(len(grid)):
            col_tuple = tuple([grid[i][j] for i in range(len(grid))])
            pairs += row_hash.get(col_tuple,0)
        return pairs
