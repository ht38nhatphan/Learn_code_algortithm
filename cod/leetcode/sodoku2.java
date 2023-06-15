package corejava;

public class sodoku2 {
	public static void main(String[] args) {
		char[][] sudoku = new char[][]{
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '4', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
        };
        sodoku2 solver = new sodoku2();
        solver.solveSudoku(sudoku);
        for (int i = 0; i < sudoku.length; i++) {
            for (int j = 0; j < sudoku[i].length; j++) {
                System.out.print(sudoku[i][j] + " ");
            }
            System.out.println();
        }
	}
	 public void solveSudoku(char[][] board) {
	        int[][] rows = new int[9][10];
	        int[][] cols = new int[9][10];
	        int[][] boxes = new int[9][10];

	        // Initialize the arrays with the known values
	        for (int i = 0; i < 9; i++) {
	            for (int j = 0; j < 9; j++) {
	                if (board[i][j] != '.') {
	                    int num = board[i][j] - '0';
	                    int boxIdx = (i / 3) * 3 + j / 3;
	                    rows[i][num] = 1;
	                    cols[j][num] = 1;
	                    boxes[boxIdx][num] = 1;
	                }
	            }
	        }

	        // Solve the sudoku using Algorithm X
	        solve(board, rows, cols, boxes, 0, 0);
	    }

	    private boolean solve(char[][] board, int[][] rows, int[][] cols, int[][] boxes, int i, int j) {
	        // If we have reached the last row, we have solved the sudoku
	        if (i == 9) {
	            return true;
	        }

	        // Calculate the row and column indices of the next cell
	        int nextI = j == 8 ? i + 1 : i;
	        int nextJ = j == 8 ? 0 : j + 1;

	        // If the cell is already filled, move to the next cell
	        if (board[i][j] != '.') {
	            return solve(board, rows, cols, boxes, nextI, nextJ);
	        }

	        // Try filling the cell with each possible value
	        for (int num = 1; num <= 9; num++) {
	            int boxIdx = (i / 3) * 3 + j / 3;
	            if (rows[i][num] == 0 && cols[j][num] == 0 && boxes[boxIdx][num] == 0) {
	                board[i][j] = (char) (num + '0');
	                rows[i][num] = 1;
	                cols[j][num] = 1;
	                boxes[boxIdx][num] = 1;
	                if (solve(board, rows, cols, boxes, nextI, nextJ)) {
	                    return true;
	                }
	                board[i][j] = '.';
	                rows[i][num] = 0;
	                cols[j][num] = 0;
	                boxes[boxIdx][num] = 0;
	            }
	        }

	        // If no value works, backtrack
	        return false;
	    }
}
