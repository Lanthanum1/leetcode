class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        ans = [0] * n
        for i, (qx, qy, qr) in enumerate(queries):
            cnt = 0
            for x, y in points:
                if (qx-x) ** 2 + (qy-y) ** 2 <= qr ** 2:
                    cnt += 1                    
            ans[i] = cnt

        return ans