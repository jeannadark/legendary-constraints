from collections import defaultdict

class UGraph:
    """Constructs an undirected unweighted graph."""
    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = list()

    def add_edge(self, src: int, dest: int) -> None:
        """Add edges between source and destination vertices.

        At the same time, append vertices to the list of vertices.
        
        :param src: source vertex
        :type src: int
        :param dest: destination vertex
        :type dest: int
        """
        self.graph[src].append(dest)
        self.graph[dest].append(src)

        # append vertices that do not exist yet to the list of vertices
        if src not in self.vertices:
            self.vertices.append(src)
        if dest not in self.vertices:
            self.vertices.append(dest)

    def get_neighbors(self, v_id: int) -> list:
        """Return the list of a vertex's neighbors.
        
        :param v_id: a given vertex id
        :type v_id: int
        :return: list of neighbors
        :rtype: list
        """
        return self.graph[v_id]
