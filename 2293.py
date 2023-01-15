class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        mn = True
        while len(nums) > 1:
            n  = len(nums)
            arr = [0] * (n//2)
            for i in range(0, n-1, 2):
                arr[i//2] = min(nums[i], nums[i+1]) if mn else max(nums[i], nums[i+1])
                mn = not mn
            nums = arr
        return nums[0]
