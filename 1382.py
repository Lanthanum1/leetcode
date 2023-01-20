# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # 通用的做法是遍历这棵树得到值数组，然后每次选取中间的元素构建新的平衡二叉树，但就这题而言，很明显是丢掉了原树是一棵二叉搜索树这一信息，但好在通用的做法时间复杂度不高
        def get_nums(node): # 得到值数组
            if node is None:
                return 
            get_nums(node.left)
            nums.append(node.val)
            get_nums(node.right)
        
        def get_avl(l, r):
            if l > r:
                return
            m = l +((r-l)>>1)
            node = TreeNode(val=nums[m])
            node.left = get_avl(l, m-1)
            node.right = get_avl(m+1, r)
            return node


        nums = []
        get_nums(root)
        return get_avl(0, len(nums)-1)