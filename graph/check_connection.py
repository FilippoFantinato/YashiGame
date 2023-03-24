from graph.graph import Graph, Vertex

def DFS_connected(G: Graph, v: Vertex, parent: Vertex, visited):
    visited[v] = True
    for u in G.get_adj_list_vertex(v):
        if u != parent:
            if not visited[u]:
                # Go on with DFS iff the vertex to visit isn't the parent 
                # and hasn't been visited yet
                DFS_connected(G, u, v, visited)


def is_connected(G: Graph) -> bool:
    '''Returns True if the first run of DFS visits all the vertices and therefore
    the number of components hasn't been incremented more than once'''
    visited = {v: False for v in G.get_vertices()}
    k = 0 # Number of connected components
    for v in G.get_vertices():
        if not visited[v]:
            k += 1
            if k != 1: # Returns False if the number of components has been incremented more than once
                return False
            DFS_connected(G, v, None, visited)

    return True