class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Each row and col must have digits 1-9 (once each - no duplicates)
        # each 3x3 sub box has digits 1-9 no duplicates
        # the board does not have to be full OR solvabale to be true
            # What this means is, we check that there are no duplicate numbers in 
            # each row, col, and 3x3 grid
        # We can use a set here since we want to eliminate duplicates. We could have 1 set for: cols, rows, 3x3 grid. The question that remains is how will we decide which grid the (r,c) pair belongs to.
        # r = 0-2, c = 0-2: Box 1
        # r = 0-2, c = 3-5: Box 2
        # r = 0-2, c = 6-8: Box 3
        # r = 3-5, c = 0-2: box 4
        # r = 3-5, c = 3-5: box 5
        # we can see that for every 3 grids, the row indicies stay the same, the col indicies change. This is equivalent to saying (r // 3, c // 3)

        rows = [set() for x in range(9)]    # 9 row sets
        cols = [set() for x in range(9)]    # 9 col sets
        boxes = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == '.': continue

                if val in cols[c] or val in boxes[(r//3, c//3)] or val in rows[r]:
                    return False
                cols[c].add(val)
                rows[r].add(val)
                boxes[(r//3, c//3)].add(val)

            
            
        return True


        