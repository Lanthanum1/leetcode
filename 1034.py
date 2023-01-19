d = [0,1,0,-1,0] # dfs 上下左右四个方向
class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        # 先 dfs 把所有连通块染色，然后再把中间块染回去
        def dfs(x, y):
            if x < 0 or x >= len(grid) or y < 0 or y>= len(grid[0]) or grid[x][y] != pre: # 越界或者不相同的颜色
                return 
            grid[x][y] = color # 染色
            mask[x][y] = 1 # 标记这个位置被染色了
            for r, c in pairwise(d):
                new_r = x + r 
                new_c = y + c 
                dfs(new_r, new_c)

        if grid[row][col] == color: # 这个是不能少的，否则如果入口元素的颜色就是要染的颜色的话，就会出不了 dfs
            # 如果入口元素的颜色和要染色的颜色不相同的话，那么从入口元素开始dfs，例如向上，当它想要向下dfs的时候，因为触发 grid[x][y] != pre 而退出。但是，如果是相同的话，那么 pre 和 染色后的颜色是相等的，这个条件不会触发，因此会一直dfs
            return grid
        m = len(grid)
        n = len(grid[0])
        pre = grid[row][col]
        mask = [[0] * n for _ in range(m)] # 用来标记是否被染色
        dfs(row, col)
        for i in range(1, m-1):# 跳过边界
            for j in range(1, n-1):
                if mask[i][j] == 1 and mask[i-1][j] == 1 and mask[i+1][j] == 1 and mask[i][j-1] == 1 and mask[i][j+1] == 1: # 判断是否为内部节点
                    grid[i][j] = pre

        return grid
        

