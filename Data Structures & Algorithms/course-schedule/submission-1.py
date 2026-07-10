
# numCourses = 2, prerequisites = [[0,1],[1,0]]

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for prerequisite in prerequisites:
            adj[prerequisite[0]].append(prerequisite[1])
        
        # {0: 1, 1:0}
        visiting = set()
        seen = set()
        def dfs(course: int) -> bool:
            if course in seen:
                return True
            elif course in visiting:
                return False
            
            visiting.add(course) # {1, 0}
            for p in adj[course]:
                if not dfs(p):
                    return False
            seen.add(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True