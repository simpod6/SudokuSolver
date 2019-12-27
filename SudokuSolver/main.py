from Sudoku import Sudoku, NUM_COLS, NUM_ROWS

grid = [[0,0,4,3,0,0,2,0,9],
[0,0,5,0,0,9,0,0,1],
[0,7,0,0,6,0,0,4,3],
[0,0,6,0,0,2,0,8,7],
[1,9,0,0,0,7,4,0,0],
[0,5,0,0,8,3,0,0,0],
[6,0,0,0,0,0,1,0,5],
[0,0,3,5,0,8,6,9,0],
[0,4,2,9,1,0,3,0,0] ]


def main():
    sudoku = Sudoku(grid)
    sudoku.solve()        
    
    outputGrid = sudoku.getGrid()

    for row in range(NUM_ROWS):
        print(outputGrid[row])


if __name__ == "__main__":
    main()
