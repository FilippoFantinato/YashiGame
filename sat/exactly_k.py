from pysat.formula import WCNF
import itertools


def exactly_k(lits, k: int) -> WCNF:
    phi = WCNF()
    n = len(lits)

    # At least k
    for sub_lits in itertools.combinations(lits, n - k + 1):
        phi.append([lit for lit in sub_lits])
        
    # At most k
    for sub_lits in itertools.combinations(lits, k + 1):
        phi.append([-lit for lit in sub_lits])

    return phi