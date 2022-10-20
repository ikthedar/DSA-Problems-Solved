class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        
        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS
                or grid[r][c] == 0 or (r, c) in visit): # if row/ column out of bounce OR current node's number is 0 OR current node is already visited and in the set
                return 0
            
            visit.add((r, c)) # after visiting node add that to the hashset
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))
        
        area = 0
        # now start traversing all the position in the graph from the beginning
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs (r, c))
        
        return area
