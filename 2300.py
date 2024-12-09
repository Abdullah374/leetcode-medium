from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        potions.sort()
        result = []

        

      

        for i in range(n):
            low = 0
            high = m -1
            while low <= high:
                mid = (high + low)//2
                product = spells[i] * potions[mid]
                if product >= success:
                    high = mid-1
                else:
                    low = mid + 1
            result.append(m - low)
            

        return result