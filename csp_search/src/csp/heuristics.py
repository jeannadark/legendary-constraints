from src.csp.csp_utils import get_number_of_conflicts
from typing import Any


def get_most_constrained_vertex(graph: Any, csp: Any) -> int:
    """Get the most constrained vertex to assign a color value to next.

	This function will search for yet unassigned vertices and choose as the next vertex to color
	the one that has most constraints, i.e. fewer possible colors to assign.
	
	:param graph: given graph
	:type graph: any
    :param csp: given csp problem
    :type csp: any
	:return: the next vertex to assign color value to
	:rtype: int
	"""
    unassigned = []
    for vertex in graph.vertices:
        if vertex not in csp.coloring.keys():
            unassigned.append(vertex)

    mrv_heuristic = lambda vertex: len(
        csp.possible_colors[vertex]
    )
    next_vertex = min(unassigned, key=mrv_heuristic)

    return next_vertex

def get_least_constraining_values(csp: Any, vertex: int) -> list:
    """Get the least constraining color value to assign next to a given vertex.
	
	This function will compute the least conflicted color value to assign.

	:param csp: given csp problem
	:type csp: any
	:param vertex: current vertex
	:type vertex: int
	:return: sorted least-conflicted color values for the current vertex
	:rtype: list
	"""
    if len(csp.possible_colors) == 1:
        return csp.possible_colors[vertex]

    lcv_heuristic = lambda color: get_number_of_conflicts(
        csp=csp, v_id=vertex, color=color
    )
    next_values = sorted(csp.possible_colors[vertex], key=lcv_heuristic)

    return next_values
