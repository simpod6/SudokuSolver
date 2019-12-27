from unittest import TestCase
from SudokuSolver.Sudoku import Sudoku, NUM_COLS, NUM_ROWS, Cell

TEST_GRID = ("530070000"
             "600195000"
             "098000060"
             "800060003"
             "400803001"
             "700020006"
             "060000280"
             "000419005"
             "000080079")

SOLUTION_GRID = ("534678912"
                 "672195348"
                 "198342567"
                 "859761423"
                 "426853791"
                 "713924856"
                 "961537284"
                 "287419635"
                 "345286179")

START_GRID_TEST_ROWS_COLS = ("034678912"
                             "602195348"
                             "190342567"
                             "859061423"
                             "426803791"
                             "713920856"
                             "961537084"
                             "287419605"
                             "345286170")

START_GRID_TEST_SQUARES = ("034608910"
                           "672195348"
                           "198342567"
                           "859761423"
                           "026803790"
                           "713924856"
                           "961537284"
                           "287419635"
                           "045206170")


class TestSudokuSolver(TestCase):
    
    def setUp(self):
        pass

    def test_grid(self):
        sudoku = Sudoku(TEST_GRID)

        outputGrid = sudoku.getGrid()
        
        self.assertEqual(outputGrid, TEST_GRID)
    
    def test_cell(self):                 
        for row in range(NUM_ROWS):
            cell = Cell()
            cell.setValue(0)
            for i in range(8):
                value = int(SOLUTION_GRID[row * NUM_COLS + i + 1])
                cell.removePossibleValue(value)
            self.assertEqual(cell.getValue(), int(SOLUTION_GRID[row * NUM_COLS]))
    
    def test_solutionRows(self):
        sudoku = Sudoku(START_GRID_TEST_ROWS_COLS)
        sudoku.solveRows()
        
        outputGrid = sudoku.getGrid()

        self.assertEqual(outputGrid, SOLUTION_GRID)
        
    
    def test_solutionCols(self):
        sudoku = Sudoku(START_GRID_TEST_ROWS_COLS)
        sudoku.solveCols()        
        
        outputGrid = sudoku.getGrid()

        self.assertEqual(outputGrid, SOLUTION_GRID)

    def test_solutionSquares(self):
        sudoku = Sudoku(START_GRID_TEST_SQUARES)
        sudoku.solveSquares()        
        
        outputGrid = sudoku.getGrid()

        self.assertEqual(outputGrid, SOLUTION_GRID)
    
    def test_isSolved(self):
        sudoku = Sudoku(START_GRID_TEST_SQUARES)
        self.assertFalse(sudoku.isSolved())

        sudoku = Sudoku(SOLUTION_GRID)
        self.assertTrue(sudoku.isSolved())
    
    def test_solve(self):
        sudoku = Sudoku(TEST_GRID)
        sudoku.solve()        
        
        outputGrid = sudoku.getGrid()

        self.assertEqual(outputGrid, SOLUTION_GRID)
