class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        a = [1] * n
        for i in range(n-1, -1, -1):
            if k - i <= 26:
                a[i] = k - i
                k -= (k-i)
            else:
                a[i] = 26
                k -= 26
        s = ''
        for x in a:
            s += chr(ord('a')+x-1)
        return s