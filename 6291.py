class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sm = 0
        for num in nums:
            a = [int(x) for x in str(num)]
            sm += sum(a)
        return sum(nums) - sm
