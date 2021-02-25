from src.csp.csp_utils import check_if_different_colors
from typing import Any

def AC3(csp: Any, queue=None) -> bool:
    """Perform AC3 arc-consistency check.

    This function will select an arc from the queue (i.e. a binary constraint)
    and keep checking for inconsistent values amongst the neighboring vertices.
    If inconsistent values have been found, the arc (next adjacent vertex, current vertex) will be
    added to the queue.

    The algorithm terminates when all arcs have been checked.

    :param csp: given csp problem
    :type csp: any
    :param queue: container storing binary constraints
    :type queue: list
    :return: true or false
    :rtype: bool
    """
    while queue:
        (xi, xj) = queue.pop()
        if remove_inconsistent_values(csp=csp, vertex_i=xi, vertex_j=xj):
            if len(csp.possible_colors[xi]) == 0:
                return False
            for Xk in csp.constraints[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
    return True


def remove_inconsistent_values(csp: Any, vertex_i: int, vertex_j: int) -> bool:
    """Remove inconsistent values.

    This function will check for inconsistent color assignments between adjacent vertices.
    If a given color in the list of possible colors of the current vertex is in conflict with
    any possible color assignment of another vertex, then that color is removed from the list
    of possible color assignments of the current vertex.
    
    :param csp: given csp problem
    :type csp: any
    :param vertex_i: current vertex
    :type vertex_i: int
    :param vertex_j: adjacent vertex
    :type vertex_j: int
    :return: true or false
    :rtype: bool
    """
    removed = False

    # for each possible value remaining for vertex i
    for color in csp.possible_colors[vertex_i]:

        # if vertex_i=color is in conflict with vertex_j=possible color
        if not any(
            [
                check_if_different_colors(color_a=color, color_b=possible_color)
                for possible_color in csp.possible_colors[vertex_j]
            ]
        ):
            # then remove vertex_i=color
            csp.possible_colors[vertex_i].remove(color)
            removed = True

    return removed
