from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        return nums[-k]