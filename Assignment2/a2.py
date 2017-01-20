# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        Initialize the rat's four instance variables.

        >>> rat = Rat('P', 1, 4)
        >>> rat.symbol
        'P'
        >>> rat.row
        1
        >>> rat.col
        4
        >>> rat.num_sprouts_eaten
        0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Set the rat's row and col instance variables to the given row and column.

        >>> rat = Rat('P', 1, 4)
        >>> rat.set_location(2, 2)
        >>> rat.row
        2
        >>> rat.col
        2
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Add one to the rat's num_sprouts_eaten variable.
        
        >>> rat = Rat('P', 1, 4)    
        >>> rat.eat_sprout()
        >>> rat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        """ (Rat) -> str

         Return a string representation of the rat, in this format:
            symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> rat = Rat('P', 1, 4)
        >>> str(rat)
        'P at (1, 4) ate 0 sprouts.'
        """
        
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Initialize this maze's four instance variables.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1),Rat('P', 1, 4))        
        >>> maze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> str(maze.rat_1)
        'J at (1, 1) ate 0 sprouts.'
        >>> str(maze.rat_2)
        'P at (1, 4) ate 0 sprouts.'
        >>> maze.num_sprouts_left
        3
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = 0
        for list in self.maze:
            for character in list:
                if character == SPROUT:
                    self.num_sprouts_left = self.num_sprouts_left + 1
        
    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Return True if and only if there is a wall at the
        given row and column of the maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  Rat('J', 1, 1),\
                  Rat('P', 1, 4))
        >>> maze.is_wall(1,6)
        True
        >>> maze.is_wall(2,1)
        False
        """

        row = self.maze[row]
        character = row[col]
        if character == WALL:
            return True
        else:
            return False

    def get_character(self, row, col):
        """ (Maze, int, int) -> bool

        Return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should be
        returned rather than HALL.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                  ['#', '.', '.', '.', '.', '.', '#'], \
                  ['#', '.', '#', '#', '#', '.', '#'], \
                  ['#', '.', '.', '@', '#', '.', '#'], \
                  ['#', '@', '#', '.', '@', '.', '#'], \
                  ['#', '#', '#', '#', '#', '#', '#']], \
                  Rat('J', 1, 1),\
                  Rat('P', 1, 4))
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.get_character(1, 4)
        'P'
        >>> maze.get_character(3, 3)
        '@'
        >>> maze.get_character(5, 3)
        '#'
        >>> maze.get_character(4, 3)
        '.'
        """
        if self.rat_1.row == row:
            if self.rat_1.col == col:
                return self.rat_1.symbol
            
        if self.rat_2.row == row:
            if self.rat_2.col == col:
                return self.rat_2.symbol
            
        row = self.maze[row]
        character = row[col]
        return character

    def move(self, rat_to_be_moved, vertical, horizontal):
        """ (Maze, Rat, int, int) -> bool

        The first parameter represents a maze, the second represents a rat,
        the third represents a vertical direction change (UP, NO_CHANGE or
        DOWN), and the fourth represents a horizontal direction change (LEFT,
        NO_CHANGE or RIGHT).

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                      ['#', '.', '.', '.', '.', '.', '#'], \
                      ['#', '.', '#', '#', '#', '.', '#'], \
                      ['#', '.', '.', '@', '#', '.', '#'], \
                      ['#', '@', '#', '.', '@', '.', '#'], \
                      ['#', '#', '#', '#', '#', '#', '#']], \
                      Rat('J', 1, 1),\
                      Rat('P', 3, 2))

        >>> maze.move(maze.rat_1, NO_CHANGE, NO_CHANGE)
        True
        >>> maze.get_character(1, 1)
        'J'
        >>> maze.move(maze.rat_1, UP, NO_CHANGE)
        False
        >>> maze.move(maze.rat_1, DOWN, NO_CHANGE)
        True
        >>> maze.get_character(2, 1)
        'J'
        >>> maze.get_character(3, 3)
        '@'
        >>> maze.num_sprouts_left
        3
        >>> maze.move(maze.rat_2, NO_CHANGE, RIGHT)
        True
        >>> maze.get_character(3, 3)
        'P'
        >>> maze.move(maze.rat_2, NO_CHANGE, LEFT)
        True
        >>> maze.get_character(3, 2)
        'P'
        >>> maze.get_character(3, 3)
        '.'
        >>> maze.num_sprouts_left
        2

        """

        # change calculation
        vertical_change = 0
        if vertical == NO_CHANGE:
            vertical_change = 0
        if vertical == UP:
            vertical_change = -1
        if vertical == DOWN:
            vertical_change = 1
        horizontal_change = 0
        if horizontal == NO_CHANGE:
            horizontal_change = 0
        if horizontal == LEFT:
            horizontal_change = -1
        if horizontal == RIGHT:
            horizontal_change = 1

        # determine new coordinates
        new_row = rat_to_be_moved.row + vertical_change
        if new_row < 0:
            return False
        new_col = rat_to_be_moved.col + horizontal_change
        if new_col < 0:
            return False
        if self.is_wall(new_row, new_col):
            return False

        # determine the character and appropriate action
        character = self.get_character(new_row, new_col)
        if character == SPROUT:
            rat_to_be_moved.eat_sprout()
            self.maze[new_row][new_col] = HALL
            self.num_sprouts_left = self.num_sprouts_left - 1
        rat_to_be_moved.set_location(new_row, new_col)
        return True

    def __str__(self):
        """ (Maze) -> str

        Returns string representation of a maze.

        >>> maze = Maze([['#', '#', '#', '#', '#', '#', '#'], \
                      ['#', '.', '.', '.', '.', '.', '#'], \
                      ['#', '.', '#', '#', '#', '.', '#'], \
                      ['#', '.', '.', '@', '#', '.', '#'], \
                      ['#', '@', '#', '.', '@', '.', '#'], \
                      ['#', '#', '#', '#', '#', '#', '#']], \
                      Rat('J', 1, 1),\
                      Rat('P', 1, 4))
        >>> print(maze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        horizontal = 0
        vertical = 0
        toPrint = ''
        for list in self.maze:
            for character in list:
                toPrint = toPrint + self.get_character(vertical, horizontal)
                horizontal = horizontal + 1
            toPrint = toPrint + '\n' 
            vertical = vertical + 1
            horizontal = 0
        toPrint = toPrint + str(self.rat_1)
        toPrint = toPrint + '\n' 
        toPrint = toPrint + str(self.rat_2)
        return toPrint
