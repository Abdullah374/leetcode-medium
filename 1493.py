from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        max_size = 0

        zero = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            max_size = max(max_size, right - left)
        return max_size
