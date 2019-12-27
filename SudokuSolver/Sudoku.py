NUM_COLS = 9
NUM_ROWS = 9

class Cell(object):    
    def __init__(self):
        self.value = 0
        self.possibleValues = [1,2,3,4,5,6,7,8,9]        
        pass
    
    def setValue(self, _value):
        self.value = _value        
    
    def getValue(self):
        return self.value
    
    def removePossibleValue(self, valueToRemove):
        if self.value == 0:
            if valueToRemove in self.possibleValues:
                self.possibleValues.remove(valueToRemove)
                if len(self.possibleValues) == 1:
                    self.value = self.possibleValues[0]
    
    





class Sudoku(object):
    grid = [[None for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
        
    def __init__(self, _grid):        
        self.grid = [ [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)] ]

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.grid[row][col].setValue(int(_grid[row*NUM_COLS+col]))
 
    def getGrid(self):        
        outGridString = ""

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):                
                outGridString = outGridString + f"{self.grid[row][col].getValue()}"

        return outGridString

    def solveRows(self):
        for row in range(NUM_ROWS):
            values = []
            for col in range(NUM_COLS):
                if self.grid[row][col].getValue() != 0:
                    values.append(self.grid[row][col].getValue())
            if len(values) != 0:
                for col in range(NUM_COLS):
                    if self.grid[row][col].getValue() == 0:
                        for value in values:
                            self.grid[row][col].removePossibleValue(value)
    
    def solveCols(self):
        for col in range(NUM_COLS):
            values = []
            for row in range(NUM_ROWS):
                if self.grid[row][col].getValue() != 0:
                    values.append(self.grid[row][col].getValue())
            if len(values) != 0:
                for row in range(NUM_ROWS):
                    if self.grid[row][col].getValue() == 0:
                        for value in values:
                            self.grid[row][col].removePossibleValue(value)
    
    def solveSquares(self):
        for squareRow in range(int(NUM_ROWS/3)):
            for squareCol in range(int(NUM_COLS/3)):
                values = []
                for row in range(3):
                    for col in range(3):
                        if self.grid[squareRow*3+row][squareCol*3+col].getValue() != 0:
                            values.append(self.grid[squareRow*3+row][squareCol*3+col].getValue())
                if len(values) != 0:
                    for row in range(3):
                        for col in range(3):
                            if self.grid[squareRow*3+row][squareCol*3+col].getValue() == 0:
                                for value in values:
                                    self.grid[squareRow*3+row][squareCol*3+col].removePossibleValue(value)
    
    def isSolved(self):
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                if self.grid[row][col].getValue() == 0:
                    return False
        return True
    
    def solve(self):
        while not self.isSolved():
            self.solveRows()
            self.solveCols()
            self.solveSquares()


                            





        