from pysat.formula import CNF

from sat.no_crossing import no_crossing
from sat.no_cycles import no_cycles
from sat.exactly_k import exactly_k


def basic_constraints(lines, points, pointsToLines) -> CNF:
    phi = CNF()

    phi_no_crossing = no_crossing(lines, points)
    phi_no_cycles = no_cycles(lines, points, pointsToLines)
    phi_tree = exactly_k(lines.keys(), len(points) - 1)

    phi.extend(phi_no_crossing.clauses)
    phi.extend(phi_no_cycles.clauses)
    phi.extend(phi_tree.clauses)

    return phi
