class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subboxes = collections.defaultdict(set) # key = (row//3, column//3)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in subboxes[(r//3, c//3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                subboxes[(r//3, c//3)].add(board[r][c])
        
        return True
