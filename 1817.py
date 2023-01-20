class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        # list 不可哈希，先转成tuple
        logs = [tuple(x) for x in logs]
        nums = list(set(logs))
        ht = Counter(nums)
        for idx, t in nums:
            ht[idx] += 1
        for k, v in ht.items():
            ans[v-1] += 1 # ans 是以 1 为下标起点的
        return ans

