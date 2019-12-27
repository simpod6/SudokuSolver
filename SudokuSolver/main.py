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
    sudoku = Sudoku(grid)
    sudoku.solve()        
    
    outputGrid = sudoku.getGrid()

    for row in range(NUM_ROWS):
        print(outputGrid[row*NUM_COLS:row*NUM_COLS+9])


if __name__ == "__main__":
    main()
