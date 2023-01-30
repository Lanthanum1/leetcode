class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # / 这个方向的斜线的横纵坐标之和是相同的
        # \ 这个方向的斜线横纵坐标之差是相同的
        ans = []
        col = [0] * n
        # 我们只需要知道每一列的皇后放在哪一行就行，具体地，从第 0 行开始遍历，选择没有被选过的列， check 横纵坐标是否满足上面的两个情况
        def dfs(r, s):
            if r == n:
                ans.append(['.'*c + 'Q' + '.'*(n-1-c) for c in col]) #对于具体的某一行，如果要放在第 c 列，那么前面有 c 个空白， 后面有 n-1-c 个空白
                return 
            for c in s:
                if all(r+c != R+col[R] and r-c != R-col[R] for R in range(r)): # for R in range(r) 意思就是 check 当前行上面的行
                    col[r] = c # 放皇后
                    dfs(r+1, s-{c}) # # 减哈希
        dfs(0, set(range(n)))
        return ans