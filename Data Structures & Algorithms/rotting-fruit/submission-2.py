from collections import deque
class Solution:

    # m x n grid with 3 possible values
    # 0. empty cell, 1: fresh fruit, 2: rotten fruit
    # if a fresh fruit is neighboring a rotten fruit (1 is next to 2),
    # the fresh fruit also becomes rotten.
    # this happens every minute - so every iteration of a grid
    # goal: return min num of mins that no 1's remain in the grid, -1 if impossible

    # BFS because we need to cover everything in the neighboring levels first, then expand
        # i need a visit set
    
    # what happens when there are multiple rotting fruit

    def orangesRotting(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])
        DIRS = ((1, 0), (-1,0), (0, 1), (0, -1))
        # visits = set()
        num_mins = 0
        fresh = 0
        
        q = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r,c))
                    # visits.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        


        while q and fresh > 0:
            level_size = len(q)

            for x in range(level_size):
                row, col = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc
                    if ((nr in range(R)) and (nc in range(C)) and
                    (grid[nr][nc] == 1)):
                        q.append((nr, nc))
                        # visits.add((nr, nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            num_mins += 1
        
        return num_mins if fresh == 0 else -1 # syntax check
        