import math
import enum
from collections import defaultdict, deque
from itertools import chain, combinations
from pysat.formula import CNF

from graph.graph import Graph


def init_graph(lines, points):
    g = Graph()

    def euclidian_distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    for (u, v) in lines.values():
        g.add_edge(u, v, euclidian_distance(points[u], points[v]))

    return g


def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


"""
class Colors(enum.Enum):
    white = 0
    red = 1
    green = 2

    def __str__(self):
        return self.value

def mark_all_cycles(
    g: Graph, v, p, cycle_number, colors: dict, parents: dict, mark: dict
):
    print("Visiting: ", v)

    # already (completely) visited vertex.
    if colors[v] == 2:
        return cycle_number

    if colors[v] == 1:
        cycle_number += 1
        cur = p
        mark[cur].append(cycle_number)

        # backtrack the vertex which are
        # in the current cycle thats found
        while cur != v:
            print("\tMarking ", cur)
            cur = parents[cur]
            mark[cur].append(cycle_number)

        return cycle_number

    parents[v] = p
    colors[v] = 1

    for u in g.get_adj_list_vertex(v):

        # if it has not been visited previously
        if v != parents[u] and u != p:
            cycle_number = mark_all_cycles(g, u, v, cycle_number, colors, parents, mark)

    colors[v] = 2

    return cycle_number

def get_cycles(mark: dict):
    cycles = defaultdict(list)

    for v in mark:
        for c in mark[v]:
            cycles[c].append(v)

    return cycles
"""

# TODO: Delete it
# def graph_xor(G1: Graph, G2: Graph):
#     g1_edges = G1.get_edges()
#     g2_edges = G2.get_edges()
#     edges = g1_edges.union(g2_edges)

#     inter = g1_edges.intersection(g2_edges)

#     return Graph(edges - inter)


def get_path_from_to(G: Graph, v, u, parents):
    path = Graph()
    cur = u
    while cur != -1 and cur != v:
        p = parents[cur]
        # print("Adding: ", cur, p)
        path.add_edge(cur, p, G.get_weight(cur, p))
        cur = p

    # path.add_edge(cur, p, G.get_weight(cur, p))

    return path


def get_fundamental_cycles(G: Graph, r):
    in_t = defaultdict(bool)
    T = Graph()
    Q = deque([r])
    parents = defaultdict(lambda: -1)
    cycles = set()

    while Q:
        v = Q.popleft()
        # print("Visiting: ", v)
        for u in G.get_adj_list_vertex(v):
            if u != parents[v]:
                # print("\tAnalyzing: ", u)
                if in_t[u]:
                    r_v_path = get_path_from_to(T, r, v, parents)
                    r_u_path = get_path_from_to(T, r, u, parents)

                    # print(f"\t\tPath 1: {r_v_path.get_edges()}")
                    # print(f"\t\tPath 2: {r_u_path.get_edges()}")
                    # print(f"\t\tCycle: {graph_xor(r_u_path, r_v_path).get_edges()}")
                    # cycle = graph_xor(r_u_path, r_v_path)
                    cycle = r_u_path ^ r_v_path
                    cycle.add_edge(u, v, G.get_weight(u, v))

                    cycles.add(cycle)
                else:
                    Q.append(u)
                    in_t[u] = True
                    T.add_edge(v, u, G.get_weight(v, u))
                    parents[u] = v

    return cycles


def get_cycles(G: Graph):
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


def constraints_no_cycles(cycles: list, pointsToLines):
    phi_no_cycles = CNF()

    for cycle in cycles:
        constraint = []
        for u, v, _ in cycle:
            constraint.append(-pointsToLines[u][v])

        if constraint:
            phi_no_cycles.append(constraint)

    return phi_no_cycles


def no_cycles(lines, points, pointsToLines):
    G = init_graph(lines, points)

    # v = list(G.get_vertices())[0]
    # p = None
    # colors = defaultdict(int)
    # parents = defaultdict(lambda: -1)
    # mark = defaultdict(list)

    # mark_all_cycles(g, v, p, 0, colors, parents, mark)

    # mark = mark_all_cycles(g, v)

    # cycles = get_cycles(mark)

    cycles = get_cycles(G)

    phi_no_cycles = constraints_no_cycles(cycles, pointsToLines)

    return phi_no_cycles
