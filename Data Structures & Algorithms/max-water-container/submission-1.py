class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # min(heights[l], heights[r]) * (r - l)
        # When the container goes narrow down, the chance to get larger container only to update the min(heights[l], heights[r])
        total = 0
        l, r = 0, len(heights) - 1
        while l < r:
            # calculate the amount
            # Update the total if the amount is larger than the current total
            # Move the lower heigth index to forward
            total = max(min(heights[l], heights[r]) * (r - l), total)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return total