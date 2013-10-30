#!/usr/bin/env python2.7

import sys
import random

from termcolor import colored

from playground import PlayGround, Position
from solver import Area, Solver, RandomStrategy

def main(args):
    print "Flood fill"

    pg = PlayGround(12, 12, 6)

    pg.fill_random()
    pg.plot()

    solver = Solver(pg, RandomStrategy(pg))
    solver.solve()

if __name__ == '__main__':
    main(sys.argv[1:])
