# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        # 无需判断 为空 的情况
        # 对于根节点，根节点肯定不为空， 如果都在左边，左子树不为空，如果都在右边，右子树也不会为空，也就是说根本不会出现当前节点为空的情况
        if p.val < x and q.val < x: # 说明 p 和 q 都在左子树， 递归左子树
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right, p, q)
        return root # p 和 q 在当前节点两侧，或当前的值等于 p 或 q
        