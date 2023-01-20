class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def dfs(x, ans):
            if len(g[x]) == 0:# 一旦遇到叶子。就把路径上的ans 加进数组中，并把 ans 清零
                time.append(ans)
                ans = 0
            ans += informTime[x]
            for v in g[x]:
                dfs(v, ans)

        g = [[] for _ in range(n)]
        for i, x in enumerate(manager):# 建树
            if x != -1:
                g[x].append(i)
        ans = 0
        time = []
        dfs(headID, ans)
        return max(time)