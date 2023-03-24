from pysat.formula import WCNF

from typing import NewType, Set, List
from itertools import chain, combinations
from collections import defaultdict, deque

from graph.graph import Graph, Edge, Vertex
from yashi_types import PointsToLine, Lines


Cycle = NewType("Cycle", Set[Edge])


def init_graph(lines: Lines) -> Graph:
    g = Graph()
    for (u, v) in lines.values():
        g.add_edge(u, v)
    return g


def powerset(iterable):
    """returns the powerset of a set"""
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def get_path_from_to(G: Graph, v: Vertex, u: Vertex, parents) -> Graph:
    """returns a graph representing the path from v to u"""
    path = Graph()
    cur = u
    while cur != None and cur != v:
        p = parents[cur]
        path.add_edge(cur, p, G.get_weight(cur, p))
        cur = p

    return path


def get_fundamental_cycles(G: Graph, r: Vertex) -> Set[Graph]:
    """returns a set of graphs represting the fundamental cycles"""
    in_t = defaultdict(bool)
    T = Graph()
    Q = deque([r])
    parents = defaultdict(lambda: None)
    cycles = set()

    while Q:
        v = Q.popleft()
        for u in G.get_adj_list_vertex(v):
            if u != parents[v]:
                if in_t[u]:
                    r_v_path = get_path_from_to(T, r, v, parents)
                    r_u_path = get_path_from_to(T, r, u, parents)
                    cycle = r_u_path ^ r_v_path
                    cycle.add_edge(u, v, G.get_weight(u, v))
                    cycles.add(cycle)
                else:
                    Q.append(u)
                    in_t[u] = True
                    T.add_edge(v, u, G.get_weight(v, u))
                    parents[u] = v

    return cycles


def get_cycles(G: Graph) -> List[Cycle]:
    """returns a list containing all the cycles got from
    the fundamental cycles"""
    r = list(G.get_vertices())[0]
    fundamental_cycles = get_fundamental_cycles(G, r)
    cycles = []
    for subset in powerset(fundamental_cycles):
        if subset:
            new_cycle = Graph()
            for cycle in subset:
                new_cycle = new_cycle ^ cycle
            cycles.append(new_cycle.get_edges())

    return cycles


def constraint_no_cycles(cycles: List[Cycle], pointsToLines: PointsToLine) -> WCNF:
    phi_no_cycles = WCNF()

    for cycle in cycles:
        constraint = []
        for u, v, _ in cycle:
            constraint.append(-pointsToLines[u][v])
        if constraint:
            phi_no_cycles.append(constraint)

    return phi_no_cycles


def no_cycles(G: Graph, pointsToLines: PointsToLine) -> WCNF:
    cycles = get_cycles(G)
    phi_no_cycles = constraint_no_cycles(cycles, pointsToLines)

    return phi_no_cycles
