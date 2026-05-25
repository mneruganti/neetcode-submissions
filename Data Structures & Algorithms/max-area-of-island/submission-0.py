class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        max_area = 0;
        visits = set()

        def dfs_area(r, c):
            curr_area = 0
            q = collections.deque()
            visits.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.pop()
                curr_area+=1
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if ((r in range(rows)) and 
                    (c in range(cols)) and 
                    ((r,c) not in visits) and 
                    grid[r][c] == 1):
                        visits.add((r,c))
                        q.append((r,c))
            return curr_area



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visits:
                    max_area = max(dfs_area(r,c), max_area)
        return max_area
        
        