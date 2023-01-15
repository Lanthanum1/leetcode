class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        if n == 1:
            return 0
        l, r = 0, 1
        ht = Counter()
        ht[nums[l]] += 1

        cnt = 0 # 统计有几对相同的数对
        while r < n and l < r: # 枚举右指针
            ht[nums[r]] += 1
            if ht[nums[r]] >= 2:
                cnt += (ht[nums[r]] - 1) # 如果前面有这个数，当前数依次和这些数配对，那么前面有几个数就增加几个
            if cnt >= k:
                ans += (n-r) # 当前满足的话，右边界右边的全部满足
            while cnt >= k: # 枚举左指针，只有在两个边界围成的数组满足 cnt >= k 时左指针才右移
                if ht[nums[l]] >= 2:   # 一旦发现当前左边界的数对cnt有贡献，那么右边有几个相同的数就减几个
                    cnt -= (ht[nums[l]] - 1)
                if cnt >= k:
                    ans += (n-r) # 同样的，如果左边界对cnt没有贡献，那么左边界更新后，右边界右边的全部满足
                ht[nums[l]] -= 1 # 把左边界在哈希计数表中减一
                l += 1
            r += 1 # 这行并不是随便放的，因为枚举左边界时也涉及到 r 
        return ans
            
            
        