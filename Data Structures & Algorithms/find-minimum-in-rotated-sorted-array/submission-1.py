class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Find the min val index
        # Think about the nums[l] ... nums[r]
        # If the "turning point" = the minimum value is in the nums[l] ... nums[r], nums[r] < nums[l].
        # Otherwise: nums[l] < nums[r]

        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r + l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]