import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_queue = []
        task_count = defaultdict(int)
        for t in tasks:
            task_count[t] += 1 # {X: 2, Y: 2}
        
        for k, v in task_count.items():
            task_queue.append((-v, k)) # ((-2, X), (-2, Y))
        
        heapq.heapify(task_queue)
        idle_queue = deque([]) # (t, -remainings, task)
        
        t = 0
        while task_queue or idle_queue:
            t += 1
            # Add a task from idle queue to the active queue
            if idle_queue and idle_queue[0][0] == t:
                nt = idle_queue.popleft()
                heapq.heappush(task_queue, (nt[1], nt[2]))
    
            if task_queue:
                remainings, task = heapq.heappop(task_queue) # -2, X -> -2, Y -> -1, X
                remainings += 1
                if remainings < 0:
                    idle_queue.append((t + n + 1, remainings, task)) # [(4, -1, X), (5, -1, Y)]
            else:
                t = idle_queue[0][0] - 1
        return t
