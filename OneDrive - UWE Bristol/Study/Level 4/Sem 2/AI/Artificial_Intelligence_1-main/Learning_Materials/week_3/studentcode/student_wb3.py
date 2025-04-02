
from approvedimports import *

class DepthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "depth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """void in superclass
        In sub-classes should implement different algorithms
        depending on what item it picks from self.open_list
        and what it then does to the openlist

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        my_index = len(self.open_list) - 1
        next_soln = self.open_list[my_index]
        self.open_list.pop(my_index)

        # <==== insert your pseudo-code and code above here
        return next_soln

class BreadthFirstSearch(SingleMemberSearch):
    """your implementation of depth first search to extend
    the superclass SingleMemberSearch search.
    Adds  a __str__method
    Over-rides the method select_and_move_from_openlist
    to implement the algorithm
    """

    def __str__(self):
        return "breadth-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements the breadth-first search algorithm

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        my_index = 0

        next_soln = self.open_list[my_index]

        self.open_list.pop(my_index)

        # <==== insert your pseudo-code and code above here
        return next_soln

class BestFirstSearch(SingleMemberSearch):
    """Implementation of Best-First search."""

    def __str__(self):
        return "best-first"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements Best First by finding, popping and returning member from openlist
        with best quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """

        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # IF IsEmpty(open_list) THEN
        if not self.open_list:
            return None
        
        # bestChild <-- GetMemberWithHighestQuality(openList)
        best_index = 0
        for i in range(len(self.open_list)):
            if self.open_list[i].quality < self.open_list[best_index].quality:
                best_index = i
        
        # RETURN bestChild (Best-First keeps the openlist to allow backtracking)
        next_soln = self.open_list.pop(best_index)

        # <==== insert your pseudo-code and code above here
        return next_soln

class AStarSearch(SingleMemberSearch):
    """Implementation of A-Star  search."""

    def __str__(self):
        return "A Star"

    def select_and_move_from_openlist(self) -> CandidateSolution:
        """Implements A-Star by finding, popping and returning member from openlist
        with lowest combined length+quality.

        Returns
        -------
        next working candidate (solution) taken from openlist
        """
        
        # create a candidate solution variable to hold the next solution
        next_soln = CandidateSolution()

        # ====> insert your pseudo-code and code below here

        # IF IsEmpty(open_list) THEN
        if not self.open_list:
            return None
        
        # bestChild <-- GetMemberWithHighestcombined(openList)
        best_index = 0
        for i in range(len(self.open_list)):
            combined_cost = len(self.open_list[i].variable_values) + self.open_list[i].quality
            best_combined_cost = len(self.open_list[best_index].variable_values) + self.open_list[best_index].quality
            if combined_cost < best_combined_cost:
                best_index = i
        
        # RETURN bestChild
        next_soln = self.open_list.pop(best_index)

        # <==== insert your pseudo-code and code above here
        return next_soln
wall_colour= 0.0
hole_colour = 1.0

def create_maze_breaks_depthfirst():
    # ====> insert your code below here
    #remember to comment out any mention of show_maze() before you submit your work

    
    maze = Maze(mazefile="maze.txt")
    
    # Place walls to create a dead-end path
    maze.contents[1][1] = wall_colour
    maze.contents[2][1] = wall_colour
    maze.contents[3][1] = wall_colour
    maze.contents[4][1] = wall_colour
    maze.contents[5][1] = wall_colour  # Dead-end path for DFS
    
    # Create another path for BFS to find the goal
    maze.contents[1][2] = hole_colour  # Alternate path for BFS
    maze.contents[2][2] = hole_colour
    maze.contents[3][2] = hole_colour
    maze.contents[3][3] = hole_colour  # Goal path for BFS
    
    # Save the maze to a file
    maze.save_to_txt("maze-breaks-depth.txt")


    # <==== insert your code above here
