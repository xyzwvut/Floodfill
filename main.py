#!/usr/bin/env python2.7

import argparse
import random
import sys

from termcolor import colored

from config import config
from playground import PlayGround, Position, FieldColorPalette
from solver import Area, Solver, RandomStrategy, MostPeripheralsStrategy, \
                   MostUnfloodedColorStrategy

def parse_cmdline(argv):
    """Parse applications commandline and feed into global config"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbosity', action='count', default=0,
                        help='increase output verbosity')
    parser.add_argument('--iterations', type=int, default=50,
                        help='number of iterations')

    args = parser.parse_args(argv)
    config['args'] = args
    config['verbosity'] = args.verbosity


def main(argv):
    parse_cmdline(argv)

    print "Flood fill"

    fp = FieldColorPalette(num_colors=6)
    pg = PlayGround(12, 12, fp)
    pg.fill_random()
    pg.plot()

    p = pg.copy()
    solver1 = Solver(p, RandomStrategy(p))
    sol1 = solver1.solve()

    p = pg.copy()
    solver2 = Solver(p, MostPeripheralsStrategy(p))
    sol2 = solver2.solve()

    p = pg.copy()
    solver3 = Solver(p, MostUnfloodedColorStrategy(p))
    sol3 = solver3.solve()

    print sol1
    print sol2
    print sol3

    if 'iterations' in config['args']:
        steps = config['args'].iterations

    print "Giving Random strategy %s tries" % steps

    bs = sol1
    for i in range(steps):
        p = pg.copy()
        solver1 = Solver(p, RandomStrategy(p))
        sol = solver1.solve()
        if sol.better_than(bs):
            bs = sol
            print bs


if __name__ == '__main__':
    main(sys.argv[1:])
