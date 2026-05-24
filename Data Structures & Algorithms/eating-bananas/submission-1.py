class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # max(piles) >= k >= sum(piles) // h
        # eating_speed(piles, k) -> O(n)
        def eating_speed(k):
            return sum([(pile // k) + (1 if pile % k else 0) for pile in piles]) if k > 0 else float('inf')
        l, r = sum(piles) // h, max(piles)
        while l < r:
            mid = (l + r) // 2
            print(l, r, mid,  eating_speed(mid))
            if eating_speed(mid) > h:
                l = mid + 1
            else:
                r = mid
        return l
