class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if (i > 0 and nums[i] == nums[i - 1]): # Skip condition
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (r < len(nums) - 1 and nums[r + 1] == nums[r]) or nums[l] + nums[r] > target:
                    r -= 1
                elif (i + 2 < l and nums[l - 1] == nums[l]) or nums[l] + nums[r] < target:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        print(result)
        return result