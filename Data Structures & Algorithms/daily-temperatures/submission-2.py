class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)
        stack = [] # store (index, temperature)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][1] < temp:
                top_i, _ = stack.pop()
                result[top_i] = i - top_i
            stack.append((i, temp))
        return result