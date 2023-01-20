d = [1,0,1]
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, r0, c0): # r0 和 c0 是记录左上角的坐标，r 和 c 是当前元素的坐标
            if  r == m  or c == n  or land[r][c] != 1:
                # 越界了或者当前不是 1，就直接返回
                return 
            land[r][c] = 2 # 标记为已遍历，避免重复计算

            for r1, c1 in pairwise(d): # 只有向下和向右两个方向
                new_r = r + r1
                new_c = c + c1
                dfs(new_r, new_c, r0, c0)
            # 4 个 or:
            # ①：整个 land 的右下角，两个遍历方向都不能走
            # ②：当前元素不是最底下那行，也不是最右边那一列，但是下面和右边的元素都是 0，被两个 0 隔断了
            # ③：当前元素不是最底下那行，但是它是最右边那一列，并且下面是 0，被下面的 0 和右边的墙隔断了
            # ③：当前元素不是最右边那列，但是它是最下边那一行，并且右边是 0，被右边的 0 和下面的墙隔断了

            if (r == m - 1 and c == n - 1) or (r + 1 < m and land[r+1][c] == 0 and c + 1 < n and land[r][c+1] == 0) or (r < m - 1 and c == n - 1 and land[r+1][c] == 0) or (c < n - 1 and r == m - 1 and land[r][c+1] == 0):
                ans.append([r0,c0,r,c])
            

        m, n = len(land), len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 :
                    dfs(i, j, i, j)
        
        return ans