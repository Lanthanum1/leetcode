# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_h(self, node):
            if node is None:
                return 0
            return max(self.get_h(node.left), self.get_h(node.right)) + 1
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 从上至下 dfs， 一旦发现左右子树等高，就返回
        if root is None:
            return root
        lh, rh = self.get_h(root.left), self.get_h(root.right)
        if lh == rh:
            return root
        return self.subtreeWithAllDeepest(root.left) if lh > rh else self.subtreeWithAllDeepest(root.right)

