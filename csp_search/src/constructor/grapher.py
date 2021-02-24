from collections import defaultdict
from src.csp.ac3 import forward_check

class UGraph:
    """Constructs an undirected unweighted graph."""

    def __init__(self):
        self.graph = defaultdict(list)
        self.vertices = list()
        self.coloring = dict()
        self.possible_colors = dict()

        self.pruned = dict()

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

    def assign_color(self, v_id: int, color: int) -> None:
        """Assign color to a vertex.
        
        :param v_id: a given vertex id
        :type v_id: int
        :param color: a given color value
        :type color: int
        """
        self.coloring[v_id] = color

    def unassign_color(self, v_id: int) -> None:
        """Unassign color from a vertex.
        
        :param v_id: a given vertex id
        :type v_id: int
        """
        if v_id in self.coloring.keys():
            for color in self.pruned[v_id]:
                self.possible_colors[v_id].append(color)
            self.pruned[v_id] = []
            del self.coloring[v_id]

    def assign_possible_color_range(self, num_of_colors: int) -> None:
        """Assign possible color values to each vertex as an initializer.
        
        :param num_of_colors: number of colors to use
        :type num_of_colors: int
        """
        for v_id in self.vertices:
            if v_id not in self.possible_colors.keys():
                self.possible_colors[v_id] = list(range(0, num_of_colors))
        self.pruned = {v: list() for v in self.vertices}
