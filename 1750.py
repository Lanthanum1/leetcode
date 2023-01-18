class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] != s[r]:
                return r - l + 1
            while l < n - 1 and s[l] == s[l+1]:
                l += 1
            while r > 0 and s[r] == s[r-1]:
                r -= 1
            l += 1
            r -= 1
        return 1 if l == r else 0 # 有可能最后左右指针指向同一个元素，也有可能错开了