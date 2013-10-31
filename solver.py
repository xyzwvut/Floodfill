import random
import uuid

from playground import Position, FieldColorPalette

# TODO: Remove
import sys
from termcolor import colored

"""
 TODO:
 - Need a way to walk the n-dimensional space in a
   controlled way, so that every field gets visited
   one time.
"""

class Area:
    """Area on the playground.
       It is identified by the leftmost highest
       elemet part of the area.
    """
    def __init__(self, pg, pos):
        self.pg = pg
        self.pos = pos

    @staticmethod
    def generate_tag():
        return uuid.uuid4().bytes

    def key_field(self):
        return self.pg.get_field(self.pos)

    def get_color(self):
        return self.key_field().get_color()

    def bordering_colors(self):
        """Find colors that give a valid next step"""
        # TODO:Return a ColorPalette
        palette = FieldColorPalette()

        def add_color(field, inside):
            if not inside:
                palette.add(field.get_color())

        self.walk(add_color)
        return palette

    def walk_helper(self, pos, color, handler, tag):
        """Helper function to walk the area

           handler expects one argument, the field

           Take the color as an argument instead of 
           using self.key_field() because the handler
           may change the color.
        """
        # Outside of the playground
        if pos == None:
            return

        field = self.pg.get_field(pos)

        if field.is_visited(tag):
            return

        # Not part of the area
        if not field.has_color(color):
            handler(field, False)
            return

        # Execute handler
        handler(field, True)

        field.set_visited(tag)

        # Visit neighbours
        self.walk_helper(pos.left(), color, handler, tag)
        self.walk_helper(pos.right(), color, handler, tag)
        self.walk_helper(pos.up(), color, handler, tag)
        self.walk_helper(pos.down(), color, handler, tag)

    def walk(self, handler):
        """Visit all fields of the area"""
        if not handler:
            return

        tag = Area.generate_tag()
        self.walk_helper(self.pos, self.get_color(), handler, tag)
        self.pg.remove_visited(tag)

    def flood(self, color):
        """Flood field with color"""
        def set_color(field, inside):
            if inside:
                field.set_color(color)

        # Skip repaint with same color
        if self.get_color().is_equal(color):
            return

        self.walk(set_color)

    def size(self):
        """Get number of fields"""
        # TODO: How to use just an int here?
        s = [0]

        def inc_counter(field, inside):
            if inside:
                s[0] = s[0] + 1

        self.walk(inc_counter)
        return s[0]


class Step:
    """A Step in the Solution
    """
    def __init__(self, color):
        self.color = color


class Solver:
    """Find the sequence of fills with the lowest number
       of steps to flood the whole board
    """
    def __init__(self, pg, strategy):
        self.pg = pg
        self.strategy = strategy
        self.area = Area(pg, Position(pg, 0, 0))

    def step(self, n):
        """Find the next step, do it"""
        color = self.strategy.next_color()

        if color == None:
            return None

        print "Step %s, picked %s" % (n, color)

        self.area.flood(color)
        return color

    def solve(self):
        # List of colors
        solution = []

        print "Solving"

        while True:

            color = self.step(len(solution))

            if color == None:
                break

            self.pg.plot()

            # Verify valid step
            solution.append(color)

        self.solution = solution
        self.print_solution()

    def print_solution(self):
        s = "Solution: "
        for c in self.solution:
            s += str(c)
        print s


class Strategy:
    """Strategy for picking the next color
    """
    def __init__(self, pg):
        self.pg = pg

    def next_color(self):
        """Color picked for the next step"""


class RandomStrategy:
    """Pick a random color"""
    def __init__(self, pg):
        self.area = Area(pg, Position(pg, 0, 0))
        pass

    def next_color(self):
        """
         1. Get color of the current flood
         2. Get all adjacent colors
         3. Pick random color from that list
        """
        palette = self.area.bordering_colors()

        if palette.num() == 0:
            return None

        print "Available Colors: %s" % palette.plot()

        # Pick a random color
        color = palette.get_a_color()
        return color


class MostPeripheralsStrategy:
    """Pick color that has the most neighbouring fields"""
    def __init__(self, pg):
        pass

    def next_color(self):
        """
         1. Get adjacent colors
         2. Get all remaining fields
         3. Group by color and count number of fields
         4. Pick first color
        """

class MostUnfloddedColorSolver:
    """Pick color that has the most unflooded fields"""
    def __init__(self, pg):
        pass

    def next_color(self):
        """
         1. Get color of current flood
         2. Get all adjacent fields
         3. Group by color count number of fields
         4. Pick first color
        """
        pass


class GeneticSolver:
    """Genetic Algorithm"""
    def __init__(self, pg):
        pass

    def next_color(self):
        """
        """
        pass

