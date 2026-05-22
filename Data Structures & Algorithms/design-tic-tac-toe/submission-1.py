class TicTacToe:

    def __init__(self, n: int):
        self._matrix = [['.' for _ in range(n)] for _ in range(n)]
        self._player1 = 1
        self._player2 = 2
        self._current_player = self._player1
        print(self._matrix)
    
    def _check_win(
        self, 
        row: int,
        col: int,
        mark: str
    ) -> bool:
        n = len(self._matrix)
        # check column
        total_marks = 0
        for r in range(n):
            if self._matrix[r][col] == mark:
                total_marks += 1
        
        if total_marks == n: 
            return True

        # check row 
        total_marks = 0
        for c in range(n):
            if self._matrix[row][c] == mark:
                total_marks += 1
        
        if total_marks == n:
            return True
        
        if row != col and row + col != n- 1:
            # row, col is not diagonal
            return False
        main_diagonal = []
        anti_diagonal = []
        for i in range(n):
            main_diagonal.append((i, i))
            anti_diagonal.append((i, n - 1 - i))
    
        total_marks = 0
        for r, c in main_diagonal:
            total_marks += 1 if self._matrix[r][c] == mark else 0
        if total_marks == n:
            return True

        total_marks = 0
        for r, c in anti_diagonal:
            total_marks += 1 if self._matrix[r][c] == mark else 0
        return total_marks == n



    def move(self, row: int, col: int, player: int) -> int:
        if self._player1 == player:
            mark = 'X' 
        else:
            mark = 'O'
        self._matrix[row][col] = mark
        if self._check_win(row, col, mark):
            return player
        return 0


        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
