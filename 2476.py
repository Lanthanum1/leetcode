# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # 对二叉搜索树中序遍历得到一个升序数组
        n = len(queries)
        nums = []
        def dfs(node):
            if not node:
                return 
            if node.left:dfs(node.left)
            nums.append(node.val)
            if node.right:dfs(node.right)
        dfs(root)
        ans = []
        # print(nums)
        # 例如 对于数组 a = [1,2,2,2,3,4]
        # bisect_right(a, 2) 就是想象在所有的 2 后面插入一个 2，也就是插入到下标 4 的位置，如果是求小于等于 2 的最大数，只需要bisect_right - 1
        # bisect_left(a, 2) 就是想象在所有的 2 前面插入一个 2，也就是插入到下标 1 的位置，正好把第一个 2 顶替了，刚好是大于等于 2 的最小数 的位置
        for x in queries:
            idx1 = bisect_right(nums, x) - 1
            idx2 = bisect_left(nums, x)
            mn = nums[idx1] if idx1 >= 0 else -1
            mx = nums[idx2] if idx2 < len(nums) else -1
            ans.append([mn, mx])          
        return ans