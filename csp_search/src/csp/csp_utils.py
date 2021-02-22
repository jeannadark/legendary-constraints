def check_if_different_colors(color_a: int, color_b: int) -> bool:
    """Check if the colors of two adjacent vertices are different.
	
	:param color_a: color of vertex a
	:type color_a: int
	:param color_b: color of vertex b
	:type color_b: int
	:return: true or false
	:rtype: bool
	"""
    check = color_a != color_b
    return check


def get_number_of_conflicts(graph, v_id: int, color: int) -> int:
    """Return the number of conflicts a given vertex has with its neighbors.

	If the color value of the neighbor is not found yet and current color exists in its set of possible values,
	then there is a conflict.

	:param graph: given graph
	:type graph: dict
	:param v_id: current vertex
	:type v_id: int
	:param color: current color
	:type color: int
	:return: number of conflicts
	:rtype: int
	"""
    cnt = 0

    for neighbor in graph.get_neighbors(v_id):
        if (
            len(graph.possible_colors[neighbor]) > 1
            and color in graph.possible_colors[neighbor]
        ):
            cnt += 1
    return cnt


def is_consistent(graph, v_id: int, color: int) -> bool:
    """Check the consistency of assignment.
	
	This function will check if the assigned color has already been assigned to an adjacent vertex.
	
	:param graph: given graph
	:type graph: dict
	:param v_id: current vertex
	:type v_id: int
	:param color: current color
	:type color: int
	:return: true or false
	:rtype: bool
	"""
    is_consistent = True

    for v, c in graph.coloring.items():
        if c == color and v in graph.get_neighbors(v_id):
            is_consistent = False

    return is_consistent
