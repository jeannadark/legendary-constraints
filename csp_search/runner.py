from src.constructor.grapher import UGraph
from src.constructor.input_reader import parse_edges, parse_number_of_colors
from src.csp.backtrack import backtrack_search


def runner(filename: str) -> None:
	"""Parses provided input data, constructs a graph and finds the CSP solution.
    
    :param filename: the name of the input file to parse
    :type filename: str
    """
	f = open(filename, "r")
	text = f.read()

	## -- parse data -- ##

	# parse edge data
	edges = parse_edges(data=text)
	# parse number of colors
	num_of_colors = parse_number_of_colors(data=text)

	## -- construct a graph -- ##

	graph = UGraph()
	for edge_info in edges:
	    vertex_from = edge_info[0]
	    vertex_to = edge_info[1]
	    graph.add_edge(vertex_from, vertex_to) # add perhaps a comparison so that two same edges don't exist

	## -- initialize color range values -- ##

	graph.assign_possible_color_range(num_of_colors = num_of_colors)

	## -- start backtrack searching -- ##

	assignment = backtrack_search(graph = graph, num_of_colors = num_of_colors)

	## -- print solution -- ##
	    
	print(assignment)


if __name__ == "__main__":

    try:
        input_file = str(input("Please enter the full filename: \n"))
        runner(filename=input_file)

    except FileNotFoundError:
        print("Invalid filename. Using default filename in this directory instead.")
        input_file = "colors.txt"
        runner(filename=input_file)
