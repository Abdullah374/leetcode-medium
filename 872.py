from typin import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        list1 = []
        list2  = []
        def collect(root, list1):
            if root is None:
                return
            if root.left is None and root.right is None:
                list1.append(root.val)
            collect(root.left, list1)
            collect(root.right, list1)
        collect(root1, list1)
        collect(root2, list2)

        return list1 == list2
            

        
            
            