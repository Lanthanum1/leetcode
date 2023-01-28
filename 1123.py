# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ht = defaultdict(int) # 建立节点值和其深度的映射关系3
        ht[root.val] = 0 # 根节点深度为0
        def get_d(node):
            if not node:
                return
            # 子节点是父节点的深度 + 1 
            if node.left:
                ht[node.left.val] = ht[node.val] + 1
                get_d(node.left)
            if node.right:
                ht[node.right.val] = ht[node.val] + 1
                get_d(node.right)
        get_d(root)
        max_d = ht[max(ht, key=ht.get)]
        cnt_max_d = 0
        # 统计有几个最深的节点
        for k, v in ht.items():
            if v == max_d:
                cnt_max_d += 1
        ans = []
        # 这个公共祖先必须包含所有最深的节点
        def dfs(node, cnt):
            # 如果是最深的叶子，cnt++
            if not node.left and not node.right and ht[node.val] == max_d:
                cnt = 1
            # 把自己的cnt 加到父节点上去
            if node.left:
                cnt += dfs(node.left, 0)
            if node.right:
                cnt += dfs(node.right, 0)
            # 因为用了前序遍历，所以找到的第一个就是最深的，然后向上返回
            if cnt == cnt_max_d:
                ans.append(node)
            return cnt
        dfs(root, 0)
        return ans[0]



