from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lower = temperatures[0]
        n = len(temperatures)
        answer = [0]*n
        stack = []
        
        
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()                    
                answer[index] = i - index
            stack.append(i)
        return answer


