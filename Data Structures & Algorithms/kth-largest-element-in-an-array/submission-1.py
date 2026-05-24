import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # use max-heap
        nums = [-n for n in nums]
        heapq.heapify(nums)

        res = None
        for _ in range(k):
            res = -heapq.heappop(nums)
        return res