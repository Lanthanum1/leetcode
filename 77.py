class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            if len(path) + i < k: # 剪枝，因为答案的长度固定，如果 path 的长度加上 i 还是小于 k ，就意味着就算剩下的 i 个全部加上去，也还是不够，所以直接 return
                return  
            if len(path) == k:
                ans.append(path.copy())
            for j in range(i, 0, -1):
                path.append(j)
                dfs(j-1)
                path.pop()
        dfs(n)
        return ans