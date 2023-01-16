MOD = 10 ** 9 + 7
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) equals to nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        # 两数之和
        ans = 0
        ht = Counter()
        for x in nums:
            # 一次遍历，获取当前数后看前面有几个和自己相同的数
            y = int(str(x)[::-1])
            ans += ht[x-y]
            ht[x-y] += 1
        return ans % MOD