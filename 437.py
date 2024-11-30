from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, currSum, preSum):
            if root is None:
                return 0
            
            currSum += root.val
            path = preSum.get(currSum-targetSum,0)
            
            preSum[currSum] = preSum.get(currSum, 0) + 1

            path += dfs(root.left, currSum, preSum)
            path += dfs(root.right, currSum, preSum)

            preSum[currSum] -= 1

            return path
        return dfs(root,0,{0:1})