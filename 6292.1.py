class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n+1) for _ in range(n+1)]
        for r1, c1, r2, c2 in queries:
            r2 += 1
            c2 += 1
            diff[r1][c1] += 1
            diff[r1][c2] -= 1
            diff[r2][c1] -= 1
            diff[r2][c2] += 1
        ans = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                ans[i][j] = ans[i][j-1] + ans[i-1][j] - ans[i-1][j-1] + diff[i-1][j-1]
        return [row[1:] for row in ans[1:]]

