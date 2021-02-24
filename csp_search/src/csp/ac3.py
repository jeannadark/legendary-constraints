from src.csp.csp_utils import check_if_different_colors


def AC3(num_of_colors: int, graph, queue=None) -> bool:
    """Perform AC3 constraint propagation."""
    # csp.support_pruning()
    while queue:
        (xi, xj) = queue.pop()
        if remove_inconsistent_values(graph=graph, vertex_i=xi, vertex_j=xj, num_of_colors = num_of_colors):
            #if len(graph.possible_colors[xi]) == 0:
            #    return False
            for Xk in graph.get_neighbors(xi):
                if Xk != xi:
                    queue.append((Xk, xi))
                    print((Xk, xi))
    return True


def remove_inconsistent_values(graph, vertex_i: int, vertex_j: int, num_of_colors: int) -> bool:
    """Remove inconsistent values."""
    removed = False

    # for each possible value remaining for vertex i
    for color in graph.possible_colors[vertex_i]:

        # if vertex_i=color is in conflict with vertex_j=possible color for each possibility
        if not any(
            [
                check_if_different_colors(color_a=color, color_b=possible_color)
                for possible_color in graph.possible_colors[vertex_j]
            ]
        ):
            # then remove vertex_i=color
            graph.possible_colors[vertex_i].remove(color)
            removed = True

    #if vertex_i not in graph.possible_colors.keys():
    #    graph.possible_colors[vertex_i] = list(range(0, num_of_colors))

    # returns true if a color has been removed
    return removed

def forward_check(graph, v_id: int, color: int):
    
    for neighbor in graph.get_neighbors(v_id):
        if neighbor not in graph.coloring.keys():
            if color in graph.possible_colors[neighbor]:
                graph.possible_colors[neighbor].remove(color)
                graph.pruned[neighbor].append(color)

# https://github.com/kakou34/map-coloring-csp/blob/master/submission.py
# https://github.com/davidxk/Sudoku-CSP/blob/master/AC3SudokuSolver.py
