class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # 以value为key 降序排列，从大的开始选，遇到label超过限制就不选，往下走
        nums = sorted(zip(values, labels), reverse = True)
        ht = Counter()
        mx = 0
        ans = []
        for x in nums:
            ht[x[1]] += 1
            mx = max(mx, ht[x[1]])
            if mx > useLimit and ht[x[1]] == mx:
                # 不仅到目前为止最大的label数超过了限制，还要当前的label数量等于最大，因为可能是前面的超过了限制，但是当前的label只是刚出现，所以这两个条件都要满足
                ht[x[1]] -= 1
                mx -= 1
                continue
            ans.append(x[0])
            if len(ans) == numWanted:
                return sum(ans)
        return sum(ans) # 这一步是不能少的，因为上面的 return 不一定满足，有可能最后 ans 的长度还是小于numWanted



