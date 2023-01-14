class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = list(set(nums))
        ht = set(nums)
        ans, mx = 0, max(nums)
        for i in range(1, mx + 1):
            g = 0
            for j in range(i, mx + 1, i):
                if j in ht:
                    g = gcd(g, j)
                    if g == i:
                        ans += 1
                        break
        return ans