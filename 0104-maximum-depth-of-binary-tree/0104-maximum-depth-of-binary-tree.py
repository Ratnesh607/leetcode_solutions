# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def Solve(root):
            if not root:
                return 0
            
            l = Solve(root.left)
            r = Solve(root.right)
            return max(l , r) + 1
 
        return Solve(root)