from unittest import TestCase
from SudokuSolver.Sudoku import Sudoku, NUM_COLS, NUM_ROWS, Cell

TEST_GRID = [ [5,3,0,0,7,0,0,0,0],
             [6,0,0,1,9,5,0,0,0],
             [0,9,8,0,0,0,0,6,0],
             [8,0,0,0,6,0,0,0,3],
             [4,0,0,8,0,3,0,0,1],
             [7,0,0,0,2,0,0,0,6],
             [0,6,0,0,0,0,2,8,0],
             [0,0,0,4,1,9,0,0,5],
             [0,0,0,0,8,0,0,7,9] ]

SOLUTION_GRID = [ [5,3,4,6,7,8,9,1,2],
                  [6,7,2,1,9,5,3,4,8],
                  [1,9,8,3,4,2,5,6,7],
                  [8,5,9,7,6,1,4,2,3],
                  [4,2,6,8,5,3,7,9,1],
                  [7,1,3,9,2,4,8,5,6],
                  [9,6,1,5,3,7,2,8,4],
                  [2,8,7,4,1,9,6,3,5],
                  [3,4,5,2,8,6,1,7,9] ]

START_GRID_TEST_ROWS_COLS =    [ [0,3,4,6,7,8,9,1,2],
                                 [6,0,2,1,9,5,3,4,8],
                                 [1,9,0,3,4,2,5,6,7],
                                 [8,5,9,0,6,1,4,2,3],
                                 [4,2,6,8,0,3,7,9,1],
                                 [7,1,3,9,2,0,8,5,6],
                                 [9,6,1,5,3,7,0,8,4],
                                 [2,8,7,4,1,9,6,0,5],
                                 [3,4,5,2,8,6,1,7,0] ]

START_GRID_TEST_SQUARES = [ [0,3,4,6,0,8,9,1,0],
                            [6,7,2,1,9,5,3,4,8],
                            [1,9,8,3,4,2,5,6,7],
                            [8,5,9,7,6,1,4,2,3],
                            [0,2,6,8,0,3,7,9,0],
                            [7,1,3,9,2,4,8,5,6],
                            [9,6,1,5,3,7,2,8,4],
                            [2,8,7,4,1,9,6,3,5],
                            [0,4,5,2,0,6,1,7,0] ]


class TestSudokuSolver(TestCase):
    
    def setUp(self):
        pass

    def test_grid(self):
        sudoku = Sudoku(TEST_GRID)

        outputGrid = sudoku.getGrid()

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.assertEqual(outputGrid[row][col], TEST_GRID[row][col])
    
    def test_cell(self):                 
        for row in range(NUM_ROWS):
            cell = Cell()
            cell.setValue(0)
            for value in SOLUTION_GRID[row][1:]:
                cell.removePossibleValue(value)
            self.assertEqual(cell.getValue(), SOLUTION_GRID[row][0])
    
    def test_solutionRows(self):
        sudoku = Sudoku(START_GRID_TEST_ROWS_COLS)
        sudoku.solveRows()
        
        outputGrid = sudoku.getGrid()

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.assertEqual(outputGrid[row][col], SOLUTION_GRID[row][col])
        
    
    def test_solutionCols(self):
        sudoku = Sudoku(START_GRID_TEST_ROWS_COLS)
        sudoku.solveCols()        
        
        outputGrid = sudoku.getGrid()

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.assertEqual(outputGrid[row][col], SOLUTION_GRID[row][col])

    def test_solutionSquares(self):
        sudoku = Sudoku(START_GRID_TEST_SQUARES)
        sudoku.solveSquares()        
        
        outputGrid = sudoku.getGrid()

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.assertEqual(outputGrid[row][col], SOLUTION_GRID[row][col])
    
    def test_isSolved(self):
        sudoku = Sudoku(START_GRID_TEST_SQUARES)
        self.assertFalse(sudoku.isSolved())

        sudoku = Sudoku(SOLUTION_GRID)
        self.assertTrue(sudoku.isSolved())
    
    def test_solve(self):
        sudoku = Sudoku(TEST_GRID)
        sudoku.solve()        
        
        outputGrid = sudoku.getGrid()

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.assertEqual(outputGrid[row][col], SOLUTION_GRID[row][col])






            
        



        


        

        

        # self.assertEqual("Unknown command!", self.commandManager.executeCommand("text", "/asdasd", self.chat_id, self.testUsers[0]))

