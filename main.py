import argparse
import pandas
from enum import Enum
from pysat.solvers import Minisat22
from pysat.examples.fm import FM
from pysat.formula import WCNF

from init_yashi_game import init_yashi_game
from yashi_plot import yashi_plot
from sat.minimum_cost_solution_constraints import minimum_cost_solution_constraints
from sat.no_cycles import init_graph
from sat.basic_constraints import basic_constraints
from graph.check_connection import is_connected


class Modes(Enum):
    existence = "existence"
    count = "count"
    count_and_plot = "count-plot"
    best = "best"

    def __str__(self):
        return self.value


def existence_solver(file):
    y_csv = pandas.read_csv(file)
    solver = Minisat22()
    lines, points, pointsToLines = init_yashi_game(y_csv)
    G = init_graph(lines)

    yashi_plot({}, points, "The game")

    if is_connected(G):
        phi = basic_constraints(G, lines, points, pointsToLines)
        solver.append_formula(phi.hard)

        solution = solver.solve()

        if solution:
            model = solver.get_model()
            model_lines = {x: lines[x] for x in model if x > 0}

            yashi_plot(model_lines, points, "The solution")
        else:
            print("No solution")
    else:
        print("No solution")


def model_counting_solver(file):
    y_csv = pandas.read_csv(file)
    solver = Minisat22()
    lines, points, pointsToLines = init_yashi_game(y_csv)
    G = init_graph(lines)

    yashi_plot({}, points, "The game")

    if is_connected(G):
        phi = basic_constraints(G, lines, points, pointsToLines)
        solver.append_formula(phi.hard)

        solution = solver.solve()

        if solution:
            n_sol = 0
            for _ in solver.enum_models():
                n_sol += 1

            print("Number of solutions: ", n_sol)
        else:
            print("No solution")

    else:
        print("No solution")


def model_counting_and_plot_solver(file):
    y_csv = pandas.read_csv(file)
    solver = Minisat22()
    lines, points, pointsToLines = init_yashi_game(y_csv)
    G = init_graph(lines)

    yashi_plot({}, points, "The game")

    if is_connected(G):
        phi = basic_constraints(G, lines, points, pointsToLines)
        solver.append_formula(phi.hard)

        solution = solver.solve()

        if solution:
            n_sol = 0
            for model in solver.enum_models():
                n_sol += 1
                model_lines = {x: lines[x] for x in model if x > 0}
                yashi_plot(model_lines, points, "Solution number: " + str(n_sol))

            print("Number of solutions: ", n_sol)
        else:
            print("No solution")
    else:
        print("No solution")


def best_solution_solver(file):
    y_csv = pandas.read_csv(file)
    lines, points, pointsToLines = init_yashi_game(y_csv)
    G = init_graph(lines)

    yashi_plot({}, points, "The game")

    if is_connected(G):
        phi_hard = basic_constraints(G, lines, points, pointsToLines)
        phi_soft = minimum_cost_solution_constraints(lines, points, pointsToLines)

        phi = WCNF()
        phi.extend(phi_hard.hard)
        phi.extend(phi_soft.soft, weights=phi_soft.wght)

        solver = FM(phi, verbose=0)

        sol = solver.compute()

        if sol:
            model = solver.model
            print("Cost of the solution: ", -sum(phi_soft.wght) + solver.cost)

            model_lines = {x: lines[x] for x in model if x > 0}
            yashi_plot(model_lines, points, "The best solution")
        else:
            print("No solution")
    else:
        print("No solution")


def init_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--mode", type=Modes, choices=list(Modes), required=True)

    return parser


def main():
    args = init_args().parse_args()
    modes = {
        Modes.existence: existence_solver,
        Modes.count: model_counting_solver,
        Modes.count_and_plot: model_counting_and_plot_solver,
        Modes.best: best_solution_solver,
    }

    modes[args.mode](args.file)


if __name__ == "__main__":
    main()
