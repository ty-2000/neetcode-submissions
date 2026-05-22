import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Use min-heap
        # heapify: log(n)
        dists = [(x**2 + y**2, i) for i, (x, y) in enumerate(points)]
        heapq.heapify(dists)
        res = []
        for _ in range(k):
            res.append(points[heapq.heappop(dists)[1]])
        return res