class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 子集型回溯 答案的角度，当前数必须选择
        n, ans, path = len(nums), [], []
        def dfs(i):
            ans.append(path.copy()) # 必须选择，因此要放在外面
            if i == n:
                return
                
            # 为了避免出现[1, 2], [2, 1]这样重复的子集，我们可以人为地约定一个顺序，也就是我们可以从 i 开始枚举 i 后面的数
            for j in range(i, n):
                path.append(nums[j]) # do
                dfs(j+1) # recursion
                path.pop() # undo
        dfs(0)
        return ans

