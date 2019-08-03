
"""
This class is the template class for the Maze solver
"""

import sys
from math import sqrt
import numpy
import queue

class MazeSolverAlgoAStar:

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
        # TODO: this is you job now :-)
        self.startMaze(0,0)
  
    # Decides whether a certain row,column grid element is inside the maze or outside
    def isInGrid(self,row,column):
        # TODO: this is you job now :-)
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
        # TODO: this is you job now :-)
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

        # TODO: Add a Unit Test Case --> Very good example for boundary tests and condition coverage
        

    # Gives a grid element as string, the result should be a string row,column
    def gridElementToString(self,row,col):
        # TODO: this is you job now :-)
        # HINT: this method is used as primary key in a lookup table
        result = ""
        result += str(row)
        result += ","
        result += str(col)
        return result
    
    # check whether two different grid elements are identical
    # aGrid and bGrid are both elements [row,column]
    def isSameGridElement(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        if (aGrid[0] == bGrid[0] and aGrid[1] == bGrid[1]):
            return True
        else:
            return False


    # Defines a heuristic method used for A* algorithm
    # aGrid and bGrid are both elements [row,column]
    def heuristic(self, aGrid, bGrid):
        # TODO: this is you job now :-)
        # HINT: a good heuristic could be the distance between to grid elements aGrid and bGrid
        manhattanDistance = abs(aGrid[0]-bGrid[0])+ abs(aGrid[1]-bGrid[1])
        return manhattanDistance

    # Generates the resulting path as string from the came_from list
    def generateResultPath(self,came_from):
        # TODO: this is you job now :-)
        # HINT: this method is a bit tricky as you have to invert the came_from list (follow the path from end to start)
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
        # TODO: this is you job now :-)
        print("XX in myMazeSolver XX")

        ################ START A STAR ################

        start = [self.startRow , self.startCol]
        end = [self.endRow, self.endCol]
        frontier = queue.PriorityQueue()
        frontier.put(start,0)
        
        startKey = self.gridElementToString(self.startRow, self.startCol)
        came_from = {}
        came_from[startKey] = None
        cost_so_far ={}
        cost_so_far[startKey] = 0
        
        while not frontier.empty():
            current = frontier.get()
            currentKey = self.gridElementToString(current[0],current[1])

            if (current[0]==end[0] and current[1]==end[1]):
                break

            print("Neighbours :" , self.getNeighbours(current[0],current[1]))
            for nextNeighbours in self.getNeighbours(current[0], current[1]):
                new_cost = cost_so_far[currentKey]+1
                nextNeighboursKey = self.gridElementToString(nextNeighbours[0], nextNeighbours[1])

                if (nextNeighboursKey not in cost_so_far or new_cost < cost_so_far[nextNeighboursKey]):
                    cost_so_far[nextNeighboursKey]=new_cost
                    priority = new_cost + self.heuristic(end,nextNeighbours)
                    frontier.put(nextNeighbours, priority)
                    came_from[nextNeighboursKey] = current
        
        ################ END A STAR ################

        path = self.generateResultPath(came_from)
        print(path,"this is my Path")

        return path
                    


    # Command for starting the solving procedure
    def solveMaze(self):
        return self.myMazeSolver()
        


if __name__ == '__main__':
    mg = MazeSolverAlgoAStar()


    # HINT: in case you want to develop the solver without MQTT messages and without always
    #       loading new different mazes --> just load any maze you would like from a file

    mg.loadMaze("/Users/nadinedussel/MazeRunner/MazeExamples/Maze1.txt")
    mg.printMaze()

    ng = mg.getNeighbours(0,1)
    print(ng)

    solutionString = mg.solveMaze()
    print(solutionString)

   
