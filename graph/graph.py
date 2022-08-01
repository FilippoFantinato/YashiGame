from collections import defaultdict
from typing import NewType, Tuple

Edge = NewType("Edge", Tuple[int, int, int])
Vertex = NewType("Vertex", int)


class Graph:
    def __init__(self, edges=[]):
        self.adj_list = defaultdict(dict)
        self.edges = set()

        for s, t, w in edges:
            self.add_edge(s, t, w)

    def get_n(self):
        """returns the number of nodes"""
        return len(self.adj_list)

    def get_m(self):
        """returns the number of edges"""
        return len(self.edges)

    def get_vertices(self):
        return self.adj_list.keys()

    def get_weight(self, s, t):
        return self.adj_list[s].get(t, None)

    def get_edges(self):
        return self.edges

    def get_adj_list_vertex(self, s):
        return self.adj_list[s].keys()

    def add_edge(self, s, t, w):
        self.adj_list[s][t] = w
        self.adj_list[t][s] = w

        self.edges.add((s, t, w))
