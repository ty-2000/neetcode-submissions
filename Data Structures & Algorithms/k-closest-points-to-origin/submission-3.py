class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ds = [(point[0]**2 + point[1]**2, point[0], point[1]) for point in points]
        heapq.heapify(ds)
        
        res = []
        for _ in range(k):
            _, px, py = heapq.heappop(ds)
            res.append([px, py])
        
        return res