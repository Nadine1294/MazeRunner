
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue

class MazeSolverAlgoBreathFirst:

    EMPTY = 0       # empty cell
    BLOCKED = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        self.dimCols = 0 
        self.dimRows = 0 
        self.startCol = 0 
        self.startRow = 0 
        self.endCol = 0 
        self.endRow = 0 
        self.grid=[[]] 
        print("Algo aufgerufen")

    # Setter method for the maze dimension of the rows
    def setDimRows(self, rows):
        print("XX SET DIM ROW XX")
        self.dimRows = rows

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        print("XX SET DIM COL XX")
        
        self.dimCols = cols
        
    # Setter method for the column of the start position 
    def setStartCol(self, col):
        self.startCol = col
        print("XX SET START COL XX: ",self.startCol)

    # Setter method for the row of the start position 
    def setStartRow(self, row):
        self.startRow = row
        print("XX SET START ROW XX: " , self.startRow)

    # Setter method for the column of the end position 
    def setEndCol(self, col):  
        self.endCol = col
        print("XX SET END COL XX: " , self.endCol)

    # Setter method for the row of the end position 
    def setEndRow(self, row):   
        self.endRow = row
        print("XX SET END ROW XX: " , self.endRow)

    # Setter method for blocked grid elements
    def setBlocked(self,row ,col):
        print("XX SET BLOCKED MAZE XX")
        self.grid[row][col] = self.BLOCKED

 
    # Start to build up a new maze
    def startMaze(self, rows, columns):
        print("XX START MAZE XX")
        self.dimRows = rows
        self.dimCols = columns

        if rows == 0 and columns == 0:
            self.startRow = self.EMPTY
            self.startCol = self.EMPTY
            self.endRow = self.EMPTY
            self.endCol = self.EMPTY
        
        self.grid = [[]]

        if rows > 0 and columns > 0:
            self.grid = numpy.empty((rows,columns), dtype=int)
            for i in range(rows):
                for j in range(columns):
                    self.grid[i][j]=0
            

    # Define what shall happen after the full information of a maze has been received
    def endMaze(self):
        print("XX END MAZE 1 XX")
        print(self.startRow, "+", self.startCol, "+", self.endRow, "+", self.endCol)
        self.grid[self.startRow][self.startCol] = self.START
        self.grid[self.endRow][self.endCol] = self.TARGET

        
        

    # just prints a maze on the command line
    def printMaze(self):
        print("XX PRINT XX")
        print(self.grid)

    # loads a maze from a file pathToConfigFile
    def loadMaze(self,pathToConfigFile):
        self.grid = numpy.loadtxt(pathToConfigFile, delimiter=',',dtype=int)
        
        self.setDimCols=self.grid.shape[0]
        self.setDimRows=self.grid.shape[1]
        self.dimCols=self.grid.shape[0]
        self.dimRows=self.grid.shape[1]
        start_arr = numpy.where(self.grid == 2)
        self.startRow=int(start_arr[0][0])
        self.startCol=int(start_arr[1][0])

        end_arr = numpy.where(self.grid == 3)
        self.endRow=int(end_arr[0][0])
        self.endCol=int(end_arr[1][0])
        

    # clears the complete maze 
    def clearMaze(self):
        self.startMaze(0,0)
  
    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        if row < 0:
            return False
        elif column < 0:
            return False
        elif row >= self.dimRows:
            return False
        elif column >= self.dimCols:
            return False
        else:
            return True


    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        neighbours =[]

        #neighbours out of Grid
        if self.isInGrid(row,column) == False:
            return neighbours 
        
        #neigbours in Blocked Elements
        if self.grid[row, column] == self.BLOCKED:
            return neighbours

       
        #row+1, row-1, column +1, column -1
        next_row = row + 1
        if (self.isInGrid(next_row, column) is True and self.grid[next_row][column] != self.BLOCKED):
            neighbours.append([next_row, column])

        previous_row = row - 1
        if (self.isInGrid(previous_row,column) is True and self.grid[previous_row][column] != self.BLOCKED):
            neighbours.append([previous_row, column])
        
        next_column = column + 1
        if (self.isInGrid(row, next_column) is True and self.grid[row][next_column] != self.BLOCKED):
            neighbours.append([row, next_column])

        previous_column = column - 1
        if (self.isInGrid(row, previous_column) is True and self.grid[row][previous_column] != self.BLOCKED):
            neighbours.append([row, previous_column]) 

        return neighbours

        

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        result = ""
        result += str(row)
        result += ","
        result += str(col)
        return result
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        if (aGrid[0] == bGrid[0] and aGrid[1] == bGrid[1]):
            return True
        else:
            return False


    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        start = [self.startRow, self.startCol]
        end = [self.endRow,self.endCol]
        current = end

        path = []
        while current != start:
            path.append(current)
            current = came_from[self.gridElementToString(current[0],current[1])]
            
        path.append(start)
        path.reverse()

        return path

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        print("XX in myMazeSolver XX")

        ################ START BREATH FIRST ################

        start = [self.startRow , self.startCol]
        frontier = queue.Queue()
        frontier.put(start)
        startKey = self.gridElementToString(self.startRow, self.startCol)
        came_from = {}
        came_from[startKey]=None
        
        while not frontier.empty():
            current = frontier.get()
            print("Current = " , current)

            for nextNeighbours in self.getNeighbours(current[0], current[1]):
                nextNeighboursKey = self.gridElementToString(nextNeighbours[0], nextNeighbours[1])
                if (nextNeighboursKey not in came_from):
                    frontier.put(nextNeighbours)
                    came_from[nextNeighboursKey] = current
        
        ################ END BREATH FIRST ################

        path = self.generateResultPath(came_from)
        print(path,"this is my Path")

        return path
                    


    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()
        


if __name__ == '__main__':
    mg = MazeSolverAlgoBreathFirst()


    mg.loadMaze("/Users/nadinedussel/MazeRunner/MazeExamples/Maze1.txt")
    mg.printMaze()

    ng = mg.getNeighbours(0,1)
    print(ng)

    solutionString = mg.solveMaze()
#    print(solutionString)