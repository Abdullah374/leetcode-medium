from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        operations = 0
        i, j = 0, len(nums)-1
        while i < j:
            cursum = nums[i] + nums[j]
            if cursum == k:
                operations += 1
                i += 1
                j -= 1
            elif cursum < k:
                i += 1
            else:
                j -= 1

        return operations
            
