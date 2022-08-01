import argparse
import pandas
from enum import Enum

from sat.init_yashi_game import init_yashi_game_sat
from sat.no_cycles import init_graph
from sat.sat_plot import sat_plot
from sat.basic_constraints import basic_constraints


class Solvers(Enum):
    graph = "graph"
    sat = "sat"

    def __str__(self):
        return self.value


class Modes(Enum):
    existence = "existence"
    count = "count"
    best = "best"

    def __str__(self):
        return self.value


def graph_solver():
    pass


def sat_existence_solver(filepath):
    y_csv = pandas.read_csv(filepath)
    lines, points, pointsToLines = init_yashi_game_sat(y_csv)
    basic_constraints(lines, points, pointsToLines)
    # sat_plot(lines, points)


def init_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--solver", type=Solvers, choices=list(Solvers), required=True)
    parser.add_argument("--mode", type=Modes, choices=list(Modes), required=True)

    return parser


def main():
    args = init_args().parse_args()
    solvers = {
        Solvers.sat: {Modes.existence: sat_existence_solver},
    }

    solvers[args.solver][args.mode](args.file)


if __name__ == "__main__":
    main()
