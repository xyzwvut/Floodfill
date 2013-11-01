#!/usr/bin/env python2.7

import sys
import random

from termcolor import colored

from playground import PlayGround, Position, FieldColorPalette
from solver import Area, Solver, RandomStrategy, MostPeripheralsStrategy

def main(args):
    print "Flood fill"

    fp = FieldColorPalette(num_colors=6)
    pg = PlayGround(12, 12, fp)
    pg.fill_random()

    p = pg.copy()
    p.plot()

    solver1 = Solver(p, RandomStrategy(p))
    solver1.solve()

    solver2 = Solver(pg, MostPeripheralsStrategy(pg))
    solver2.solve()

    solver1.print_solution()
    solver2.print_solution()


if __name__ == '__main__':
    main(sys.argv[1:])
