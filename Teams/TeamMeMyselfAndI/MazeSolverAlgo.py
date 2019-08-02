
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue

class MazeSolverAlgo:

    EMPTY = 0       # empty cell
    BLOCKED = 1    # cell with obstacle / blocked cell
    START = 2       # the start position of the maze (red color)
    TARGET = 3      # the target/end position of the maze (green color)

    def __init__(self):
        # TODO: this is you job now :-)
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
        # TODO: this is you job now :-)
        self.dimRows = rows

    # Setter method for the maze dimension of the columns
    def setDimCols(self, cols):
        print("XX SET DIM COL XX")
        # TODO: this is you job now :-)
        self.dimCols = cols
        
    # Setter method for the column of the start position 
    def setStartCol(self, col):
        # TODO: this is you job now :-)
        self.startCol = col
        print("XX SET START COL XX: ",self.startCol)

    # Setter method for the row of the start position 
    def setStartRow(self, row):
        # TODO: this is you job now :-)
        self.startRow = row
        print("XX SET START ROW XX: " , self.startRow)

    # Setter method for the column of the end position 
    def setEndCol(self, col):  
        # TODO: this is you job now :-)
        self.endCol = col
        print("XX SET END COL XX: " , self.endCol)

    # Setter method for the row of the end position 
    def setEndRow(self, row):   
        # TODO: this is you job now :-)
        self.endRow = row
        print("XX SET END ROW XX: " , self.endRow)

    # Setter method for blocked grid elements
    def setBlocked(self,row ,col):
        print("XX SET BLOCKED MAZE XX")
        # TODO: this is you job now :-)
        self.grid[row][col] = self.BLOCKED

 
    # Start to build up a new maze
    # HINT: don't forget to initialize all member variables of this class (grid, start position, end position, dimension,...)
    def startMaze(self, rows, columns):
        print("XX START MAZE XX")
        # TODO: this is you job now :-)
        #HINT: populate grid with dimension row,column with zeros
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
        # TODO: this is you job now :-)
        # HINT: did you set start position and end position correctly?
        print(self.startRow, "+", self.startCol, "+", self.endRow, "+", self.endCol)
        self.grid[self.startRow][self.startCol] = self.START
        self.grid[self.endRow][self.endCol] = self.TARGET

        
        

    # just prints a maze on the command line
    def printMaze(self):
        print("XX PRINT XX")
        # TODO: this is you job now :-)
        print(self.grid)

    # loads a maze from a file pathToConfigFile
    def loadMaze(self,pathToConfigFile):
        # check whether a function numpy.loadtxt() could be useful
        # TODO: this is you job now :-)
        pass

    # clears the complete maze 
    def clearMaze(self):
        # TODO: this is you job now :-)
        self.startMaze(0,0)
  
    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        # TODO: this is you job now :-)
        pass


    # Returns a list of all grid elements neighboured to the grid element row,column
    def getNeighbours(self,row,column):
        # TODO: this is you job now :-)
        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        pass

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        # TODO: this is you job now :-)
        # HINT: this method is used as primary key in a lookup table
        pass
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        pass


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        pass

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
        pass

    #############################
    # Definition of Maze solver algorithm
    #
    # implementation taken from https://www.redblobgames.com/pathfinding/a-star/introduction.html
    #############################
    def myMazeSolver(self):
        # TODO: this is you job now :-)
        pass

    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()


if __name__ == '__main__':
    mg = MazeSolverAlgoTemplate()


    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    #mg.loadMaze("..\\MazeExamples\\Maze1.txt")
    #solutionString = mg.solveMaze()
    #print(solutionString)
   
