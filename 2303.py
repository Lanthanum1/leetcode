class Solution:
    def calculateTax(self, nums: List[List[int]], income: int) -> float:
        ans = 0
        nums.insert(0, [0, 0])
        n = len(nums)
        for i in range(1, n):
            if nums[i][0] <= income:
                ans += (nums[i][0] - nums[i-1][0]) * nums[i][1] / 100
            else:
                ans += (income - nums[i-1][0]) * nums[i][1] / 100
                break
        return ans