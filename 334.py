from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float('inf')
        second = float('inf')

        for number in nums:
            if number <= first:
                first = number
            elif number <= second:
                second = number
            else:
                return True
        return False

        