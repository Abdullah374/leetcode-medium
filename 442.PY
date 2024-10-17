from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        memo = [0] * (len(nums)+1)
        result = []
        for num in nums:
            memo[num] += 1
            if memo[num] > 1:
                result.append(num)
        return result