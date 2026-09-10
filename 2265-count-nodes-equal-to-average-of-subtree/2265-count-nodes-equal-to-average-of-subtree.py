# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def solve(root):
            if not root:
                return (0, 0)

            leftSum, leftCount = solve(root.left)
            rightSum, rightCount = solve(root.right)
            SUM = leftSum + rightSum + root.val
            COUNT = leftCount + rightCount + 1
            avg = SUM // COUNT
            if avg == root.val:
                self.result += 1
            return (SUM, COUNT)
        solve(root)
        return self.result