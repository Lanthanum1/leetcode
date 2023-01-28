class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c == '|':
                cnt += 1
                continue
            if cnt % 2 == 0 and c == '*':
                ans += 1
        return ans