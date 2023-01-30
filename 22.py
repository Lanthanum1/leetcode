class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        m = 2 * n
        path = [''] * m
        # l 是指从左往右枚举，枚举到第 i 位的时候，有几个左括号
        def dfs(i, l):
            if i == m:
                ans.append(''.join(path))
                return 
            if l < n : # 如果左括号数量小于 n， 就还能放左括号
                path[i] = '('
                dfs(i+1, l+1) # l + 1
            if i - l < l : # 如果右括号的个数小于左括号的个数，就还能放左括号
                path[i] = ')'
                dfs(i+1, l) #因为放的是左括号，l 不变
        dfs(0, 0)
        return ans