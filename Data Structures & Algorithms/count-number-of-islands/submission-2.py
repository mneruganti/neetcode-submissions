from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R, C = len(grid), len(grid[0])
        num_islands = 0
        DIRS = ((1,0),(-1, 0),(0, 1),(0, -1))
        visits = set()

        def bfs(r, c):
            q = deque()
            visits.add((r,c))
            q.append((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc
                    
                    if ((nr in range(R)) and (nc in range(C)) and
                    ((nr,nc) not in visits) and grid[nr][nc] == "1"):
                        q.append((nr, nc))
                        visits.add((nr, nc))

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r,c) not in visits:
                    bfs(r,c)
                    num_islands += 1 
        return num_islands       