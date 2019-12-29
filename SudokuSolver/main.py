from Sudoku import Sudoku, NUM_COLS, NUM_ROWS
import csv

grid = ("004300209"
        "005009001"
        "070060043"
        "006002087"
        "190007400"
        "050083000"
        "600000105"
        "003508690"
        "042910300" )


def main():    
    with open('.\SudokuSolver\data\sudoku.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                sudoku = Sudoku(row[0])            
                sudoku.solve()
                outputGrid = sudoku.getGrid()
                if outputGrid == row[1]:
                    print(f"Sudoku {line_count} solved!")
                else:
                    print(f"!!! Sudoku {line_count} NOT solved !!!")
                del sudoku
            line_count += 1
        print(f'Processed {line_count} Sudokus')


    """
    sudoku = Sudoku(grid)
    sudoku.solve()        
    
    outputGrid = sudoku.getGrid()

    for row in range(NUM_ROWS):
        print(outputGrid[row*NUM_COLS:row*NUM_COLS+9])
    """

if __name__ == "__main__":
    main()
