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
    pg.plot()

    #solver = Solver(pg, RandomStrategy(pg))
    solver = Solver(pg, MostPeripheralsStrategy(pg))
    solver.solve()

if __name__ == '__main__':
    main(sys.argv[1:])
