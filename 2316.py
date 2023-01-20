class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(u, cnt):
            mark[u] = cnt # 染色
            for v in g[u]:
                if mark[v] == 0: # 未被染色就 dfs
                    dfs(v, cnt)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = 0
        c = 1 # 标记连通块
        mark = [0] * n
        
        for i in range(n):
            if mark[i] == 0: # 未被染色就 dfs 分块
                dfs(i, c) 
                c += 1 # 用下一种颜色
        ht = Counter(mark) # 对连通块进行计数，统计有多少个连通块和每个连通块有多少个元素

        for k, v in ht.items():
            ans += v * (n-v)
        return ans//2 # 去重

        

        




