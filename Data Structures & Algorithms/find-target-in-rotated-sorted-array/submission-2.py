class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Within the "nums", there's only a point that the two adjacent (including the last-beginning) element is dropping
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            # l <= mid < r
            # if nums[mid] < nums[r] => any nums pair from num[mid] ... num[r] is always increasing
            #    if nums[mid] < target < nums[r] => target is in mid + 1 ... r
            # if nums[mid] > nums[r] => there's dropping point between mid and r
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # nums[mid] > nums[r]
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1