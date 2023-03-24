from typing import NewType, Tuple
from collections import defaultdict

Edge = NewType("Edge", Tuple[float, float, float])
Vertex = NewType("Vertex", float)


class Graph:
    def __init__(self, edges=[]):
        """build an object starting from a set of edges"""
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
        """returns all the vertices"""
        return self.adj_list.keys()

    def get_weight(self, s, t):
        """given s and t vertices,
        if exist an edge between s and t it returns the weight,
        otherwise it returns None"""
        return self.adj_list[s].get(t, None)

    def get_edges(self):
        """returns all the edges"""
        return self.edges

    def get_adj_list_vertex(self, s):
        """if s exists it returns the adjacent list of the vertex s, otherwhise None"""
        return self.adj_list[s].keys()

    def add_edge(self, s, t, w=1):
        """given s, t and w it creates the edges from s to t
        with weight w and vice-versa in the adjacent list
        and add them to the set of edges"""
        self.adj_list[s][t] = w
        self.adj_list[t][s] = w

        self.edges.add((s, t, w))
        self.edges.add((t, s, w))

    def remove_edge(self, s, t):
        """given s and t, if exist an edge between them it will be deleted"""
        w = self.adj_list[s].get(t, None)
        if w != None:
            del self.adj_list[s][t]
            del self.adj_list[t][s]
            self.edges.remove((s, t, w))
            self.edges.remove((t, s, w))

    def __eq__(self, other: object) -> bool:
        """given an another graph it checks if they have the same edges"""
        return self.edges == other.edges

    def __hash__(self):
        """returns the hash of the edges"""
        return hash(frozenset(self.edges))

    def __xor__(self, other):
        """returns a new graph made up by
        all the non common edges between two graphs"""
        g1_edges = self.get_edges()
        g2_edges = other.get_edges()

        edges = g1_edges.union(g2_edges)
        inter = g1_edges.intersection(g2_edges)

        return Graph(edges - inter)

    def __str__(self) -> str:
        return f"{self.edges}"

    def __repr__(self) -> str:
        return self.__str__()
