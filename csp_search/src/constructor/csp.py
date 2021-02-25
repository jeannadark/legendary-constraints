from typing import Any


class CSP:
    """Handles color assignments and generates constraints for a classic CSP problem."""
    def __init__(self, vertices: list):
        self.coloring = dict()
        self.possible_colors = dict()
        self.constraints = {v_id: [] for v_id in vertices}

    def initialize_color_range(self, num_of_colors: int, vertices: list) -> None:
        """Assign possible color values to each vertex as an initializer.
        
        :param num_of_colors: number of colors to use
        :type num_of_colors: int
        :param vertices: list of graph vertices
        :type vertices: list
        """
        for v_id in vertices:
            if v_id not in self.possible_colors.keys():
                self.possible_colors[v_id] = list(range(0, num_of_colors))

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
            del self.coloring[v_id]

    def generate_vertex_constraints(self, v_id: int, graph: Any) -> None:
        """Generate the list of vertices with which the current vertex has constraints.

        :param v_id: a given vertex id
        :type v_id: int
        :param graph: a given graph
        :type graph: any
        """
        for neighbor in graph.get_neighbors(v_id):
            self.constraints[v_id].append(neighbor)
