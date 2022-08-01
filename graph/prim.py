from graph.graph import Graph
from priority_queue.priority_queue import PriorityQueue
from priority_queue.vertex_helper import VertexHelper


def prim(g, s=1):
    Q = PriorityQueue()
    mst = Graph()
    in_mst = {}
    vertices = {}

    for v in g.get_vertices():
        item = VertexHelper(v, float("inf") if v != s else 0, None)
        Q.insert(item)
        vertices[v] = item
        in_mst[v] = False

    while len(Q):
        u = Q.extract_min()

        if u.parent:
            mst.add_edge(u.get_parent().get_name(), u.get_name(), u.get_priority())

        in_mst[u.name] = True

        for v in g.get_adj_list_vertex(u.name):
            if not in_mst[v]:
                new_priority = g.get_weight(u.name, v)
                vertex = vertices[v]

                if new_priority < vertex.get_priority():
                    vertex.parent = u
                    Q.decrease_key(v, new_priority)

    return mst
