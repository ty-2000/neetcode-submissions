class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # numbers[i] <= numbers[j] if i < j
        # if numbers[i] + numbers[j] > target AND ~i are not the index1 -> index2 is smaller than j 
        # if numbers[i] + numbers[j] < target AND j~ are not the index2 -> index1 is larger than j 
        i, j = 0, len(numbers) - 1
        while i < j:
            cur = numbers[i] + numbers[j]
            if cur < target:
                i += 1
            elif cur > target:
                j -= 1
            else:
                return [i + 1, j + 1]