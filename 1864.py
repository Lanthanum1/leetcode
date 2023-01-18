class Solution:
    def minSwaps(self, s: str) -> int:
        # 最终只有两种情况 '01010101....010101' or '10101010...101010'
        # 最终 0 和 1 的个数要么相等，要么相差一个
        n = len(s)
        n0 = s.count('0')
        n1 = s.count('1')
        if n0 > n1 + 1 or n1 > n0 + 1:
            return -1
        # 如果字符串中 0 和 1 的个数差异超过 1， 那么必然是不可能的，因为所有操作只有交换，而没有产生新的数
        ss0, ss1 = '', ''
        zero = False
        for i in range(n):
            if zero:
                ss1 += '0'
                ss0 += '1'
            else:
                ss1 += '1'
                ss0 += '0'
            zero = not zero
        ans1, ans0 = 0, 0
        for i in range(n):
            if s[i] != ss1[i]:
                ans1 += 1
            if s[i] != ss0[i]:
                ans0 += 1
        # print('ans0 = ', ans0, ' ', 'ans1 = ', ans1)
        # 如果可以交换，那么差异必然是偶数
        # 这两个差异中，如果只有一个是偶数，那么就返回它除以2
        # 如果两个都是偶数，说明两个都能实现，要取 min 
        if ans1 % 2 == 0 and ans0 % 2 == 0:
            return min(ans1, ans0) // 2
        if ans1 % 2 == 0 and ans0 % 2 != 0:
            return ans1 // 2
        if ans1 % 2 != 0 and ans0 % 2 == 0:
            return ans0 // 2
        return -1




