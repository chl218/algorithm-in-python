# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
                
        if not root:
            return []
        
        lview = self.rightSideView(root.left)
        rview = self.rightSideView(root.right)
                
        llen = len(lview)
        rlen = len(rview)
        
        if rview:
            if llen > rlen:
                return [root.val] + rview + lview[rlen:]
            else:
                return [root.val] + rview 
        else:
            return [root.val] + lview