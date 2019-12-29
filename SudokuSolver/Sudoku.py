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
    
    def getPossibleValues(self):
        return self.possibleValues
    
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
        iteration = 0
        while not self.isSolved() and iteration < (NUM_COLS * NUM_ROWS):
            self.solveRows()
            self.solveCols()
            self.solveSquares()
            self.solveHiddenSinglesRows()
            self.solveHiddenSinglesCols()
            self.solveHiddenSinglesSquares()
            iteration = iteration + 1
        return iteration
    
    def solveHiddenSinglesRows(self):
        for row in range(NUM_ROWS):
            possibleValuesCount = [0] * NUM_COLS
            for col in range(NUM_COLS):
                if self.grid[row][col].getValue() == 0:
                    possibleValues = self.grid[row][col].getPossibleValues()
                    for value in possibleValues:
                        possibleValuesCount[value-1] = possibleValuesCount[value-1] + 1
            for col in range(NUM_COLS):
                value = self.grid[row][col].getValue()
                if value != 0:
                    possibleValuesCount[value-1] = 0

            hiddenSingle = 0
            for i, valueCount in enumerate(possibleValuesCount):
                if valueCount == 1:
                    hiddenSingle = i + 1
            if hiddenSingle != 0:
                for col in range(NUM_COLS):
                    if self.grid[row][col].getValue() == 0:
                        possibleValues = self.grid[row][col].getPossibleValues()
                        if hiddenSingle in possibleValues:
                            self.grid[row][col].setValue(hiddenSingle)
    
    def solveHiddenSinglesCols(self):
        for col in range(NUM_COLS):
            possibleValuesCount = [0] * NUM_ROWS
            for row in range(NUM_ROWS):
                if self.grid[row][col].getValue() == 0:
                    possibleValues = self.grid[row][col].getPossibleValues()
                    for value in possibleValues:
                        possibleValuesCount[value-1] = possibleValuesCount[value-1] + 1
            for row in range(NUM_ROWS):
                value = self.grid[row][col].getValue()
                if value != 0:
                    possibleValuesCount[value-1] = 0

            hiddenSingle = 0
            for i, valueCount in enumerate(possibleValuesCount):
                if valueCount == 1:
                    hiddenSingle = i + 1
            if hiddenSingle != 0:
                for row in range(NUM_ROWS):
                    if self.grid[row][col].getValue() == 0:
                        possibleValues = self.grid[row][col].getPossibleValues()
                        if hiddenSingle in possibleValues:
                            self.grid[row][col].setValue(hiddenSingle)

    def solveHiddenSinglesSquares(self):
        for squareRow in range(int(NUM_ROWS/3)):
            for squareCol in range(int(NUM_COLS/3)):
                possibleValuesCount = [0] * NUM_ROWS
                for row in range(3):
                    for col in range(3):
                        if self.grid[squareRow*3+row][squareCol*3+col].getValue() == 0:                            
                            possibleValues = self.grid[squareRow*3+row][squareCol*3+col].getPossibleValues()
                            for value in possibleValues:
                                possibleValuesCount[value-1] = possibleValuesCount[value-1] + 1
                for row in range(3):
                    for col in range(3):
                        value = self.grid[squareRow*3+row][squareCol*3+col].getValue()
                        if value != 0:
                            possibleValuesCount[value-1] = 0

                hiddenSingle = 0
                for i, valueCount in enumerate(possibleValuesCount):
                    if valueCount == 1:
                        hiddenSingle = i + 1
                if hiddenSingle != 0:
                    for row in range(3):
                        for col in range(3):
                            if self.grid[squareRow*3+row][squareCol*3+col].getValue() == 0:
                                possibleValues = self.grid[squareRow*3+row][squareCol*3+col].getPossibleValues()
                                if hiddenSingle in possibleValues:
                                    self.grid[squareRow*3+row][squareCol*3+col].setValue(hiddenSingle)