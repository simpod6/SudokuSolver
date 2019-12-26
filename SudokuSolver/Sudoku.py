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
    # grid = [[]]
    grid = [ [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)],
             [Cell() for i in range(NUM_COLS)] ]

        
    def __init__(self, _grid):        
        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                self.grid[row][col].setValue(_grid[row][col])
        pass
    
    def getGrid(self):
        outGrid = [list() for row in range(NUM_ROWS)]

        for row in range(NUM_ROWS):
            for col in range(NUM_COLS):
                outGrid[row].append(self.grid[row][col].getValue())
        return outGrid

        