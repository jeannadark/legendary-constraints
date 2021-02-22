from src.csp.csp_utils import get_number_of_conflicts


def get_most_constrained_vertex(graph) -> int:
    """Get the most constrained vertex to assign a color value to next.

	This function will search for yet unassigned vertices and choose as the next vertex to color
	the one that has most constraints, i.e. most neighbors.
	
	:param graph: given graph
	:type graph: dict
	:return: the next vertex to assign color value to
	:rtype: int
	"""
    unassigned = []
    for vertex in graph.vertices:
        if vertex not in graph.coloring.keys():
            unassigned.append(vertex)

    mrv_heuristic = lambda vertex: len(
        graph.get_neighbors(vertex)
    )
    next_vertex = max(unassigned, key=mrv_heuristic)

    return next_vertex


def get_least_constraining_values(graph, vertex: int) -> list:
    """Get the least constraining color value to assign next to a given vertex.
	
	This function will compute the least conflicted color value to assign.

	:param graph: given graph
	:type graph: dict
	:param vertex: current vertex
	:type vertex: int
	:return: sorted least-conflicted color values for the current vertex
	:rtype: list
	"""
    if len(graph.possible_colors) == 1:
        return graph.possible_colors[vertex]

    lcv_heuristic = lambda color: get_number_of_conflicts(
        graph=graph, v_id=vertex, color=color
    )
    next_values = sorted(graph.possible_colors[vertex], key=lcv_heuristic)

    return next_values
