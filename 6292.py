class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        # 二维差分
        # 左上角和右下角加一，右上角和左下角减一
        mat = [[0 for _ in range(n)] for _ in range(n)]
        for q in queries:
            row1, col1, row2, col2 = q
            mat[row1][col1] += 1
            if row2 < n -1 and col2 < n -1:  
                mat[row2+1][col2+1] += 1
            if col2 < n -1:
                mat[row1][col2+1] -= 1
            if row2 < n -1: 
                mat[row2+1][col1] -= 1
        # 对同一行求前缀和
        for i in range(n):
            for j in range(1, n):
                mat[i][j] += mat[i][j-1]
        # 对同一列求前缀和
        for i in range(1, n):
            for j in range(n):
                mat[i][j] += mat[i-1][j]
        return mat
            
        