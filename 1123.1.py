# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 获得节点高度
        def get_h(node):
            if not node:
                return 0
            l, r = 0, 0
            if node.left:
                l = get_h(node.left)
            if node.right:
                r = get_h(node.right)
            return max(l, r) + 1
        ans = TreeNode()
        def dfs(node):
            # 左右子树等高：返回当前节点
            # 递归更高的子树
            nonlocal ans
            if not node:
                return 
            l, r = 0, 0
            if node.left:
                l = get_h(node.left)
            if node.right:
                r = get_h(node.right)
            if l == r :
                ans = node
                return 
            elif l > r:
                dfs(node.left)
            else:
                dfs(node.right)
        dfs(root)
        return ans




