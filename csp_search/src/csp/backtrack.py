from typing import Any
from src.csp.csp_utils import is_consistent
from src.csp.heuristics import (
    get_most_constrained_vertex,
    get_least_constraining_values,
)
from src.csp.ac3 import AC3


def backtrack_search(csp: Any, graph: Any) -> Any:
    """Perform backtrack search.

    This function will pick up the most constrained vertex from the list of unassigned vertices and
    try assigning the least constraining color to it. After that, the algorithm will check if the
    assignment is consistent (i.e. that it has not been assigned to any other vertex) and if yes, then
    perform an arc consistency check upon which keep recursively backtracking until all vertices have colors
    assigned to them.

    If the color assignment is not consistent, then the given color is unassigned from the vertex.
    
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
