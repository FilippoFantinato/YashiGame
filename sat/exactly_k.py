from pysat.formula import CNF
import itertools


def exactly_k(lits, k):
    phi = CNF()
    # At least k
    for sub_lits in itertools.combinations(lits, len(lits) - k + 1):
        phi.append([lit for lit in sub_lits])

    # At most k
    for sub_lits in itertools.combinations(lits, k + 1):
        phi.append([-lit for lit in sub_lits])

    return phi
