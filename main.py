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
    print solver1.solve()

    p = pg.copy()
    solver2 = Solver(p, MostPeripheralsStrategy(p))
    print solver2.solve()

    p = pg.copy()
    solver3 = Solver(p, MostUnfloodedColorStrategy(p))
    print solver3.solve()


if __name__ == '__main__':
    main(sys.argv[1:])
