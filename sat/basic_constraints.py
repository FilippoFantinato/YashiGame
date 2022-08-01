from sat.no_crossing import no_crossing
from sat.no_cycles import no_cycles


def basic_constraints(lines, points, pointsToLines):
    phi_no_crossing = no_crossing(lines, points)
    phi_no_cycles = no_cycles(lines, points, pointsToLines)
