class Solution:
    def __init__(self):
        self.visited = set()
        
    def findCircleNum(self, M: List[List[int]]) -> int:
        circles = 0
        length = len(M)
        for i in range(length):
            if i not in self.visited:
                circles += 1 # add a friend circle if not already seen
                self.dfs(i, length, M) #subsequent runs should fill visited up, not seen indicates new circle
        return circles
        
    
    def dfs(self, person, num_people, matrix):
        for i in range(num_people):
            if matrix[person][i] == 1 and i not in self.visited:
                self.visited.add(i)
                self.dfs(i, num_people, matrix)