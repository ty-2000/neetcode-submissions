class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Consume tasks step by step
        # How to detemine which task should be consumed in each step
        # At the step i, most remaining task should be selected
        # We need to track the earliest time each task can be consumed

        # tracking the number of remaining, the earliest time the task can be consumed (and the task str)
        # each element: [-number of remaining, ealiest index, task str]
        task_map = {}
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1

        remainings: list[list[int, int, str]] = []
        for k, v in task_map.items():
            remainings.append([v, 0, k])
        
        # Sort by the number of remainig task in decending order
        remainings.sort(reverse=True)

        # Consume the tasks step-by-step
        t = 0
        while remainings[0][0]: # While tasks remain
            print(t, remainings)

            # Determin the taks to be consumed
            task_index = -1
            for i in range(len(remainings)):
                if remainings[i][1] <= t:
                    task_index = i
                    break
            if task_index == -1:
                # if no task can be consumed, then skip
                t += 1
                continue
            else:
                # Consume the task
                remainings[task_index][0] -= 1
                # Set the new earliest time
                remainings[task_index][1] = t + n + 1
                # Sort again
                remainings.sort(reverse=True)
                # Increment time
                t += 1
        return t