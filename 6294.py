class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = 0
        def dfs(x, fa):
            nonlocal ans
            max_yes = p = price[x] # 带上端点
            max_no = 0 # 不带
            for y in g[x]:
                if y == fa: continue # 把它的父节点排除，遍历子树
                yes, no = dfs(y, x) # 递归子树
                ans = max(ans, yes + max_no, no + max_yes) # 子树带端点加上自己不带端点，子树不带端点加上自己带端点
                max_yes = max(max_yes, yes + p)
                max_no = max(max_no, no + p)
                # 利用子树返回的结果更新max_yes和max_no， max_no中也要加上 p 是因为如果当前是端点（叶子），那么就不会进入 for 循环，如果不是端点，本来就是要加的
            return max_yes, max_no
        dfs(0, -1)
        return ans