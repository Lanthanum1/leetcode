class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split(' ')
        s2 = sentence2.split(' ')
        l1, l2, r1, r2 = 0, 0, len(s1) - 1, len(s2) - 1
        while l1 <= r1 and l2 <= r2:
            if s1[l1] == s2[l2]:
                l1 += 1
                l2 += 1
            elif s1[r1] == s2[r2]:
                r1 -= 1
                r2 -= 1
            else:
                return False
        return True