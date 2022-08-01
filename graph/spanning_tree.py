from graph.graph import Graph, Vertex, Edge
from typing import List
import itertools


def DFS_cycle(g: Graph, v: Vertex, parent: Vertex, visited: List[bool]) -> bool:
    visited[v] = True

    for n in g.get_adj_list_vertex(v):
        if n != parent:
            if visited[n]:
                return True
            else:
                cycle = DFS_cycle(g, n, v, visited)

                if cycle:
                    return True

    return False


def is_acyclic_and_connected(g: Graph) -> bool:
    visited = {i: False for i in g.get_vertices()}
    k = 0

    for v in g.get_vertices():
        if not visited[v]:
            cycle = DFS_cycle(g, v, -1, visited)
            k += 1

            if cycle:
                return False

    return k == 1


def get_all_planar_trees(g: Graph) -> List[List[Edge]]:
    spanning_trees = []
    combs_edges = itertools.combinations(g.get_edges(), g.get_n())

    print(g.get_m())

    for comb_edges in combs_edges:
        g_st = Graph(comb_edges)
        if is_acyclic_and_connected(g_st):
            spanning_trees.append(g_st)

    return spanning_trees
