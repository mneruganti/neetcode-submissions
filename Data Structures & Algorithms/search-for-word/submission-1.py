class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

    # only move horizontally and vertically? 
        # correct.
    # Only uppercase or lower as well?
        # could have lowercase
    # how are duplicate answers handled?
        # doesn't matter
    
    # Rough Outline
    # 1. DFS 
    # 2. Loop through the rows and columns of the grid
        # If the current element (board[r][c] == word[0]):
            # count = 1
            # Run dfs(r, c, count) -> run dfs on 0,2
    # 3. return False

    # Rough Outline of dfs(r,c, count):
    # 1. Create DIRS Tuple: DIRS= ((0, 1), (1, 0), (0, -1), (-1, 0)) 
    # 2. Keep a counter of how long current word is as we explore 
    # 3. Base Case: If grid[r][c] == word[len(words) - 1] and count == len(word):
        # return True
    # 4. Loop through al DIRS:
        # for dr, dc in DIRS:
            # nr, nc = r + dr, c + dc
            # if (0 <= nr < R and 0 <= nc < C and grid[nr][nc] == word[count]):
                # dfs(nr, nc, count + 1)
        
        path = set()
        def dfs(r, c, i):
            # DIRS= ((0, 1), (1, 0), (0, -1), (-1, 0))
            if (i == len(word)):
                return True
            
            if (r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] != word[i] or (r,c) in path):
                return False
            
            path.add((r,c))
            # for dr,dc in DIRS:
                # nr, nc = r + dr, c + dc
            res = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
            path.remove((r,c))
            return res

        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (board[r][c] == word[0]):
                    if dfs(r, c, 0): return True
        return False

