class Solution:

    # 1 = land, 0 = water
    # return number of islands (count)
    # dfs

    # 1. tuple called DIRS = ((1,0),(-1, 0),(0, 1),(0, -1))
    # create a dfs helper
        # check bounds (edges + if grid[r][c] != 1) -> return 
        # grid[r][c] = 0 -> this ensures that we don't recount an island
        # dfs(r + dr, c + dc) where dr, dc are tuples from DIRS
        # we will init a counter, and create a nested for loop to go through R and C
        # inside loop, if grid[r][c] == 1
            # increase count, run dfs on r, c
        # return count
    
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = ((1,0),(-1, 0),(0, 1),(0, -1))
        R, C = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= R or c >= C or grid[r][c] != '1':
                return
            grid[r][c] = '0' # dont recount islands

            for (dr, dc) in DIRS:
                dfs(r + dr, c + dc)

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count



        