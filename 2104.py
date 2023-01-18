class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # 单调栈
        n = len(nums)
        mn, mx = [], []
        lmin, rmin, lmax, rmax = [-1] * n, [n] * n, [-1] * n, [n] * n
        for i in range(n):
            # 找到 nums[i] 左侧严格小于它的最近元素位置, 以及右侧小于等于它的最近元素位置 
            # mx 是一个递增的单调栈
            while mn and nums[mn[-1]] >= nums[i]:
                top = mn.pop()
                rmin[top] = i # 对于栈顶元素来说，当前元素就是右侧小于等于它的最近元素位置 
            lmin[i] = mn[-1] if mn else -1 # 如果此时单调栈中还有元素，那么经过前面 pop 掉所有比当前数更大的元素后，栈顶元素就是 nums[i] 左侧严格小于它的最近元素
            mn.append(i)

            # 找到 nums[i] 左侧严格大于它的最近元素位置, 以及右侧大于等于它的最近元素位置 
            # mx 是一个递减的单调栈
            while mx and nums[mx[-1]] <= nums[i]:
                top = mx.pop()
                rmax[top] = i # 对于栈顶元素来说，当前元素就是右侧大于等于它的最近元素位置 
            lmax[i] = mx[-1] if mx else -1 # 如果此时单调栈中还有元素，那么经过前面 pop 掉所有比当前数更小或相等的元素后，栈顶元素就是 nums[i] 左侧严格大于它的最近元素
            mx.append(i)

        ans = 0
        # 对于每一个元素 nums[i], 以这个元素作为最大值最左可延伸至lmax[i], 最右可以延伸至 rmax， 左右端点运用乘法原理，共有(i - lmax[i]) * (rmax[i] - i)个子数组的max是nums[i]
        for i in range(n):
            ans += nums[i] * (i - lmax[i]) * (rmax[i] - i) - nums[i] * (i - lmin[i]) * (rmin[i] - i)
        return ans
            