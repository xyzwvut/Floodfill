import sys
import random

from termcolor import colored

# TODO:
# - Make 0 special color

class ColorPalette:
    fg = ('white', 'blue', 'cyan', 'magenta',
          'green', 'red', 'yellow')
    bg = ('on_white', 'on_blue', 'on_cyan', 'on_magenta',
          'on_green', 'on_red', 'on_yellow')

    class OutOfColorsException(Exception):
        pass

    def __init__(self, num_colors=0):
        if num_colors == 0:
            num_colors = len(ColorPalette.fg)

        if num_colors > len(ColorPalette.fg):
            raise OutOfColorsException
            return None

        self.num_colors = num_colors

    def get_fg_color(self, num):
        return self.fg[num]
    
    def get_bg_color(self, num):
        return self.bg[num]

    def get_a_fg_color(self):
        idx = self.get_random_idx()
        return self.fg[idx]
    
    def get_a_bg_color(self):
        idx = self.get_random_idx()
        return self.bg[idx]


class FieldColorPalette:
    """Set of possible field colors
       Specifically set foreground and background colors
    """

    def __init__(self, palette=ColorPalette(), num_colors=0, colors=[]):
        self.colors = []

        # Specific colors given
        if colors:
            self.colors = colors
            return

        # Construct field colors
        for idx in range(0, num_colors):
            c = FieldColor(palette.get_fg_color(idx),
                           palette.get_bg_color(idx))
            self.colors.append(c)

    def add(self, field_color):
        """Add color to palette"""
        for c in self.colors:
            if c.is_equal(field_color):
                return

        self.colors.append(field_color)

    def num(self):
        """Number of colors in the palette"""
        return len(self.colors)

    def get_random_idx(self):
        return random.randint(0, self.num() - 1)

    def get_a_color(self):
        idx = self.get_random_idx()
        return self.colors[idx]

    def get_color(self, num):
        return self.colors[num]

    def plot(self):
        """Return palette field color string"""
        s = ""
        for c in self.colors:
            s += "%s" % str(c)
        return s


class FieldColor:
    """Color from a palette"""

    def __init__(self, fg, bg):
        self.fg = fg
        self.bg = bg

    def __str__(self):
        return colored(' ', self.fg, self.bg)

    def is_equal(self, color):
        return self.get_fg_color() == color.get_fg_color() and \
               self.get_bg_color() == color.get_bg_color()

    def get_fg_color(self):
        return self.fg

    def get_bg_color(self):
        return self.bg


class Field:
    """Field on the playground"""

    def __init__(self, palette):
        self.palette = palette
        self.color = palette.get_color(0)
        self.visited = {}

        # TODO: x,y coordinates?
        # TODO: Neighbours?
        # TODO: n-dimensional?

    def has_color(self, color):
        return self.color.is_equal(color)

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def set_a_color(self):
        self.color = self.palette.get_a_color()

    def set_visited(self, tag):
        self.visited[tag] = True

    def is_visited(self, tag):
        return tag in self.visited

    def remove_visited(self, tag):
        self.visited.pop(tag, None)

    def plot(self):
        sys.stdout.write(colored(' ', self.color.fg, self.color.bg))


class PlayGroundDimension:
    """Dimension of the Playground

       Will allow us to generically walk through the field
       - next()
       - prev()
       - neighbours()
    """
    pass


class Position:
    """Position on the field"""

    # TODO: Iterate over dimensions
    class InvalidPosition(Exception):
        pass

    def __init__(self, pg, x, y):
        if x < 0 or y < 0:
            raise InvalidPosition
            return None
        self.x = x
        self.y = y
        self.pg = pg

    def left(self):
        if self.x - 1 < 0:
            return None
        else:
            return Position(self.pg, self.x - 1, self.y)

    def right(self):
        if self.x + 1 >= self.pg.x:
            return None
        else:
            return Position(self.pg, self.x + 1, self.y)

    def up(self):
        if self.y - 1 < 0:
            return None
        else:
            return Position(self.pg, self.x, self.y - 1)

    def down(self):
        if self.y + 1 >= self.pg.y:
            return None
        else:
            return Position(self.pg, self.x, self.y + 1)


class PlayGround:
    """Playground""" 

    class OutOfBoundsException(Exception):
        pass

    def __init__(self, x, y, num_colors):
        """Dimensions x, y, number of colors available"""
        self.x = x
        self.y = y
        self.palette = FieldColorPalette(num_colors=num_colors)
        self.field = [[Field(self.palette) for i in range(x)] for i in range(y)]

    def inside(self, pos):
        """Is position inside the field"""
        if pos.x <= self.x and pos.y <= self.y:
            return True
        else:
            return False

    def fill_random(self):
        """Fill the field with random"""
        for i in range(self.x):
            for j in range(self.y):
                self.field[i][j].set_a_color()

    def plot(self):
        """Plot the playground"""
        for x in range(self.x):
            for y in range(self.y):
                self.field[x][y].plot()
            print ""

    def get_field(self, pos):
        """Get a field by position"""
        if not self.inside(pos):
            return None
        else:
            return self.field[pos.x][pos.y]

    def remove_visited(self, tag):
        """Remove a visited tag from all fields"""
        for i in range(self.x):
            for j in range(self.y):
                self.field[i][j].remove_visited(tag)

