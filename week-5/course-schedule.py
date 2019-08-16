class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        prereqs = defaultdict(list)
        visited = [0 for i in range(numCourses)]
        
        # fill in prereqs dictionary
        for course, req in prerequisites:
            prereqs[course].append(req)
            
        def dfs(index):
            if visited[index] == -1:
                return False # there is a cycle
            
            elif visited[index] == 1: # marked as such after visiting neighbors
                return True
            
            # mark first pass
            visited[index] = -1
            
            # visit adjacent nodes
            for adj in prereqs[index]:
                if not dfs(adj):
                    return False
            
            # mark complete
            visited[index] = 1
            
            return True # no cycle was found
        
        return all(dfs(num) for num in range(numCourses))