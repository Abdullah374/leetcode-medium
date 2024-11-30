from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxlength = 0
        def dfs(root, prev, length):
            nonlocal maxlength
            if root is None:
                return
            
            maxlength = max(maxlength, length)

            if prev =='left':
                dfs(root.left,'right', length + 1)
                dfs(root.right, 'left',1)
            else:
                dfs(root.right,'left', length + 1)
                dfs(root.left, 'right',1)
        dfs(root.left,"right", 1)
        dfs(root.right, 'left',1)
    
        return maxlength

      
             

        
