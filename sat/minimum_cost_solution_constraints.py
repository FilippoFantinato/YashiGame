import math
from pysat.formula import WCNF


def euclidian_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def minimum_cost_solution_constraints(lines, points, pointsToLines) -> WCNF:
    phi = WCNF()
    for (u, v) in lines.values():
        phi.append(
            [pointsToLines[u][v]], weight=-euclidian_distance(points[u], points[v])
        )
    return phi
