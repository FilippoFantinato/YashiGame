from pysat.formula import WCNF

from sat.no_crossing import no_crossing
from sat.no_cycles import no_cycles
from sat.exactly_k import exactly_k

from init_yashi_game import Lines, Points, PointsToLine
from graph.graph import Graph


def basic_constraints(G: Graph, lines: Lines, points: Points, pointsToLine: PointsToLine) -> WCNF:
    phi = WCNF()
    k = len(points) - 1

    phi_no_crossing = no_crossing(lines, points)
    phi_no_cycles = no_cycles(G, pointsToLine)
    phi_tree = exactly_k(lines.keys(), k)

    phi.extend(phi_no_crossing.hard)
    phi.extend(phi_no_cycles.hard)
    phi.extend(phi_tree.hard)

    return phi
