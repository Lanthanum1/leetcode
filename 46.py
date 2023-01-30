class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        path = [] * n
        # s 是一个哈希表，是还没选的数
        def dfs(i, s):
            if i == n:
                ans.append(path.copy())
                return 
            for x in s:
                path.append(x)
                dfs(i+1, s-{x})
                path.pop()
        dfs(0, set(nums))
        return ans