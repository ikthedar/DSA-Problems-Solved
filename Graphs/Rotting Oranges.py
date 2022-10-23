class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() # since we are implementing BFS algo, need to have queue ds
        time, fresh = 0, 0 # keep track of the time of every bfs layer and remaining fresh oranges
        
        ROWS, COLS = len(grid), len(grid[0]) # as always for my graph solutions, get the dimensions of the grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # if fresh add to the fresh count
                    fresh += 1
                if grid[r][c] == 2: # if rotten, add to the queue
                    q.append([r, c])
                    
            
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0: # while queue is not empty and there is still fresh orange, the loop will run
            
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    
                    if (row < 0 or row == len(grid) or
                        col < 0 or col == len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

    
