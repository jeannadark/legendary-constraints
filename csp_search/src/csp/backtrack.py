from typing import Any
from src.csp.csp_utils import is_consistent
from src.csp.heuristics import (
    get_most_constrained_vertex,
    get_least_constraining_values,
)
from src.csp.ac3 import AC3, forward_check


def backtrack_search(graph, num_of_colors: int) -> Any:
    """Perform backtrack search.
	
	:param graph: given graph
	:type graph: dict
	:return: coloring result
	:rtype: Any
	"""
    if len(graph.coloring) == len(graph.vertices):
        return graph.coloring

    next_vertex = get_most_constrained_vertex(graph=graph)

    for color in get_least_constraining_values(graph=graph, vertex=next_vertex):
        if is_consistent(graph=graph, v_id=next_vertex, color=color):
            graph.assign_color(v_id=next_vertex, color=color)
            #try: 
            #    AC3(
            #        graph=graph,
            #        queue=[(Xk, next_vertex) for Xk in graph.get_neighbors(next_vertex)],
            #        num_of_colors=num_of_colors,
            #   )
            #except:
            forward_check(graph=graph, v_id = next_vertex, color = color)
        result = backtrack_search(graph=graph, num_of_colors=num_of_colors)
        if result:
            return result
        graph.unassign(v_id=next_vertex)

    return None
