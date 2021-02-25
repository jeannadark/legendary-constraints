from typing import Any
from src.csp.csp_utils import is_consistent
from src.csp.heuristics import (
    get_most_constrained_vertex,
    get_least_constraining_values,
)
from src.csp.ac3 import AC3


def backtrack_search(csp: Any, graph: Any) -> Any:
    """Perform backtrack search.
    
    :param csp: given csp problem
    :type csp: any
    :param graph: given graph
    :type graph: any
    :return: coloring result
    :rtype: Any
    """
    if len(csp.coloring) == len(graph.vertices):
        return csp.coloring

    next_vertex = get_most_constrained_vertex(graph=graph, csp=csp)

    for color in get_least_constraining_values(csp=csp, vertex=next_vertex):
        csp.assign_color(v_id=next_vertex, color=color)
        if is_consistent(csp=csp, v_id=next_vertex, color=color):
            
            if AC3(
                csp=csp,
                queue=[(Xk, next_vertex) for Xk in csp.constraints[next_vertex]],
            ):
                result = backtrack_search(csp=csp, graph=graph)
            
                if result:
                    return result

        csp.unassign_color(v_id=next_vertex)
    return None
