class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # Store the temp value with index into a stack
        # For each element, compare the current temp with the stack's top element
        # While the cur temp equals to or is colder (smaller) than the top element, pop the stack. During popping, write the number of days from the top element to the cur element into a result
        result = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                # pop stack
                # add them into a result
                top = stack.pop()
                print(top)
                result[top[1]] = i - top[1]
            stack.append([temp, i])
        return result
