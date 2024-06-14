import unittest
import game
import maze

class TestGame(unittest.TestCase):

    def test1_example_test(self):
##########################################################################################################################
        '''Regular Maze Test'''
        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(3, 3)
        # Use this method to create test mazes
        grid._set_maze([["*",  2,  "*"],
                        [4,   "*",   2],
                        [8,    3,  "*"], ])
        start = (0,2)
        end = (1,1)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 2)
        self.assertEqual(path, [(0, 2), (0, 1), (1, 1)])

        '''Impossible Maze Test Case'''
        grid = maze.Maze(3, 3)

        grid._set_maze([["*",  "*",  "S"],
                        ["*",   "F",   "*"],
                        [8,    "*",  4], ])
        
        start = (0,2)
        end = (1,1)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        self.assertEqual(score, -1)
        self.assertEqual(path, [(0, 2)])

        '''No Walls Test'''
        grid = maze.Maze(3, 3)

        grid._set_maze([[5,  4, "S"],
                        [5,  "F", 3],
                        [6,   6,  7], ])
        
        start = (0,2)
        end = (1,1)
        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        self.assertEqual(score, 36)
        self.assertEqual(path,[(0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (1, 1)])

        '''Start and End next to each other'''
        grid = maze.Maze(3, 3)

        grid._set_maze([[5,  4,   5],
                        [5, "F", "S"],
                        [6,  "*",  7], ])
        
        start = (1,2)
        end = (1,1)

        grid.set_start_finish(start, end)
        testgame = game.Game(grid)
        score, path = testgame.find_route(start[0], start[1], 0, list())

        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        self.assertEqual(score, 19)
        self.assertEqual(path, [(1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (1, 1)])
        print(path)

if __name__ == '__main__':
    unittest.main()
