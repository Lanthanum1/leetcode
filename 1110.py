# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node, pa):
            if node is None:return node 
            l, r = node.left, node.right # 先把孩子存起来，因为现在这个节点有可能是要删除的，存起来避免伤及无辜
            if node.val in ht: # 删除
                node = None 
            elif pa is None: # 父节点被删除，那么自己就是这个家庭的顶梁柱了 
                ans.append(node)
            dfsl = dfs(l, node) # 递归左右孩子
            dfsr = dfs(r, node)
            if node: # 当前节点没有被删除的话，把处理过的孩子接回去
                node.left = dfsl
                node.right = dfsr
            return node


        if root is None:return ans
        ans = []
        ht = set(to_delete)
        dfs(root, None)
        return ans
