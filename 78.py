class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 子集型回溯 输入的角度，考虑是否当前数
        n, ans, path = len(nums), [], []
        def dfs(i):
            if i == n:
                ans.append(path.copy()) # 深拷贝
                return
            dfs(i+1) # 不选择第 i 个，直接往下递归

            # 选择第 i 个
            path.append(nums[i]) # do
            dfs(i+1) # recursion
            path.pop() # undo
        dfs(0)
        return ans

