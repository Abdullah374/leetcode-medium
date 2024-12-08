import heapq
from typing import List

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = [ (n1,n2) for n1,n2 in zip(nums1, nums2)]
        pairs.sort(key=lambda x:x[1], reverse=True)

        minheap = []
        n1Sum = 0
        n2Min = float('inf')
        res = 0              
        
        for n1, n2  in pairs:
            n1Sum += n1
            heapq.heappush(minheap, n1)

            if len(minheap) > k:
                n1pop = heapq.heappop(minheap)
                n1Sum -= n1pop
            if len(minheap)==k:
                res = max(res,n1Sum*n2)
        return res