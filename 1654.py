class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        odd_l = [0] * n 
        even_l = [0] * n
        even_l[0] = nums[0]
        # 分别统计奇偶前缀和
        for i in range(1, n):
            if i % 2 == 1:
                odd_l[i] = nums[i] + odd_l[i-1]
                even_l[i] = even_l[i-1]
            else:
                even_l[i] = nums[i] + even_l[i-1]
                odd_l[i] = odd_l[i-1]
        cnt = 0
        # 枚举每一个下标，当前下标后面的奇偶反转，前面的不变
        for i, x in enumerate(nums):
            if i % 2 == 1:
                # 如果删除的是奇数下标，那么奇数和是当前下标奇数前缀和减去自身（左边的奇数和），再加上偶数总和 - 当前偶数前缀和（奇偶反转，这是右边的奇数和），偶数和是当前下标偶数前缀和（左边的偶数和），加上奇数总和 - 当前奇数前缀和（奇偶反转，这是右边的偶数和）
                if odd_l[i] - x + even_l[-1] - even_l[i] == even_l[i] + odd_l[-1] - odd_l[i]:   
                    cnt += 1
            else:
                # 如果删除的是偶数下标，那么偶数和是当前下标偶数前缀和减去自身（左边的偶数和），再加上奇数总和 - 当前奇数前缀和（奇偶反转，这是右边的偶数和），奇数和是当前下标奇数前缀和（左边的奇数和），加上偶数总和 - 当前偶数前缀和（奇偶反转，这是右边的奇数和）
                if odd_l[i] + even_l[-1] - even_l[i] == even_l[i] - x + odd_l[-1] - odd_l[i]:
                    cnt += 1
        return cnt

