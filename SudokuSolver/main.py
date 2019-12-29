from Sudoku import Sudoku, NUM_COLS, NUM_ROWS
import csv
import time

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
    startTime = time.time()

    with open('.\SudokuSolver\data\sudoku.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        notSolved = []
        for row in csv_reader:
            if line_count > 1:
                sudoku = Sudoku(row[0])            
                iterations = sudoku.solve()
                outputGrid = sudoku.getGrid()
                if outputGrid == row[1]:
                    # print(f"Sudoku {line_count} solved in {iterations} iterations!")
                    pass
                else:
                    print(f"!!! Sudoku {line_count} NOT solved !!!")
                    notSolved.append(line_count)
                del sudoku
            line_count += 1
            if line_count % 1000 == 0:             
                print(f'Processed {line_count} Sudokus')
    stopTime = time.time()
    timeTaken = stopTime - startTime
    print(f'Processed {line_count} Sudokus in {timeTaken} seconds: {line_count/timeTaken} sudoku/second')    
    if len(notSolved) == 0:
        print("All Sudokus were solved")
    else:
        print(f"{len(notSolved)} Sudokus were not solved:")
        print(notSolved)



    """
    sudoku = Sudoku(grid)
    sudoku.solve()        
    
    outputGrid = sudoku.getGrid()

    for row in range(NUM_ROWS):
        print(outputGrid[row*NUM_COLS:row*NUM_COLS+9])
    """

if __name__ == "__main__":
    main()
