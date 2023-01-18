class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 长度为 k 的 01 串数量为 2 ** k
        # s 中去重后的所有长度为 k 的子串应该等于 2 ** k
        n = len(s)
        ht = set()
        for i in range(0, n-k+1):
            ht.add(s[i:i+k])
        return len(ht) == 2 ** k