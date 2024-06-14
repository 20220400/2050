import maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''

    def __init__(self, maze):
        self._maze = maze

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)

    def try_move(self, currow, curcol, curscore,curpath): 
        '''Until puzzle is solved in next move calls find_route (recursion) (if puzzle not possible returns (-1, curpath))'''
        if self._maze.is_move_in_maze(currow, curcol) and self._is_move_available(currow, curcol, curpath) and not self._maze.is_wall(currow, curcol):
            val = self._maze.make_move(currow,curcol,curpath)
            if self._is_puzzle_solved(currow, curcol) == True:
                 return (curscore+val, curpath)
            else:
                return self.find_route(currow, curcol, curscore+val, curpath)
        else:
            return(-1,curpath)

    def find_route(self, currow, curcol, curscore, curpath):
        '''Functions that returns the best path and highscore (called for recursion in try_move)'''
        if self._maze.get_start() == (currow, curcol):
            curscore = self._maze.make_move(currow, curcol, curpath)
        highscore = -1
        best_path = []

        # row = [currow, currow+1, currow]
        # col = [curcol, curcol+1, curcol-1]

        for i in range(4):
            # up 
            if i == 0:
                score,path = self.try_move(currow - 1,curcol, curscore, list(curpath))
            # down
            if i == 1:
                score,path = self.try_move(currow + 1, curcol, curscore, list(curpath))
            # right
            if i == 2:
                score,path = self.try_move(currow, curcol + 1, curscore, list(curpath))
            # left
            if i == 3:
                score,path = self.try_move(currow, curcol - 1, curscore, list(curpath))
            
            # highscore and bestpath
            if score >= highscore:
                highscore = score
                best_path = path
        return highscore, best_path 
    
# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(3, 3)
    
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    
    grid.init_random(0,9) # Initialze to a random board
    grid.add_random_walls(0.2)   # Make a certian percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (2,2)
    finish = (1,2)
    grid.set_start_finish(start, finish)

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")

