class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 子集型回溯，当前数必须选择
        n, ans, path = len(s), [], []
        def dfs(i):
            if i == n:
                ans.append(path.copy()) # 并不是每次都要添加，只有全部分割完毕才添加
                return

            for j in range(i, n):
                ss = s[i:j+1]
                if ss == ss[::-1]:
                    path.append(ss) # do
                    dfs(j+1) # recursion
                    path.pop() # undo
        dfs(0)
        return ans