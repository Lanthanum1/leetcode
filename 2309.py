class Solution:
    def greatestLetter(self, s: str) -> str:
        ht = set(s)
        for i in range(26, -1, -1):
            if chr(ord('a')+i) in ht and chr(ord('A')+i) in ht:
                return chr(ord('A')+i)
        return ""