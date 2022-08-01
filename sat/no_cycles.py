from collections import defaultdict
import math
from graph.graph import Graph


def init_graph(lines, points):
    g = Graph()
    for (u, v) in lines.values():
        g.add_edge(u, v, euclidian_distance(points[u], points[v]))

    return g


def euclidian_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mark_all_cycles(
    g: Graph, v, p, cycle_number, colors: dict, parents: dict, mark: dict
):
    # already (completely) visited vertex.
    if colors[v] == 2:
        return cycle_number

    if colors[v] == 1:
        cycle_number += 1
        cur = p
        mark[cur] = cycle_number

        # backtrack the vertex which are
        # in the current cycle thats found
        while cur != v:
            cur = parents[cur]
            mark[cur] = cycle_number

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
        cycles[mark[v]].append(v)

    return cycles

def constraints_no_cycles(cycles: dict):
    phi_no_cycles = 


def no_cycles(lines, points, pointsToLines):
    g = init_graph(lines, points)

    colors = defaultdict(int)
    parents = defaultdict(lambda: -1)
    mark = defaultdict(int)
    mark_all_cycles(g, 0, None, 0, colors, parents, mark)
    cycles = get_cycles(mark)

    

    return 1
