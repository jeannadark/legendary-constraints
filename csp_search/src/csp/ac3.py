from src.csp.csp_utils import check_if_different_colors
from typing import Any

def AC3(csp: Any, queue=None) -> bool:
    """Perform AC3 constraint propagation.

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

        # if vertex_i=color is in conflict with vertex_j=possible color for each possibility
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
