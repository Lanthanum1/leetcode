class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l, ans, cnt = 0, 0, 0
        ht = Counter()
        for x in nums:
            cnt += ht[x]
            ht[x] += 1
            ans += l  # 如果 l 向右移动了，那么 cnt 必然是大于等于 k 的，也就是说当前以l，r为边界的子数组一定是满足条件的，那么l左边的也全部满足条件 
            while cnt >= k:
                ans += 1 # 锁定右边界移动左边界，如果满足条件，每次ans都要+1
                ht[nums[l]] -= 1
                cnt -= ht[nums[l]]
                l += 1
        return ans

                
