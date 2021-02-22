import re


def parse_edges(data: str, string_to_split_on: str = "# Graph:",) -> list:
    """Return a list of edges.
    
    This function will parse through the read-in input data after the string ''string_to_split_on''
    to return the filtered text following that string.
    This text is then converted to a list of sub-lists, where each sub-list is of the form:
    [from_vertex, to_vertex].

    :param data: read-in input file
    :type data: str
    :param string_to_split_on: starting string to search from, defaults to '# Graph:'
    :type string_to_split_on: str
    :return: a list of lists of edges
    :rtype: list
    """
    # split the data on the string
    list_of_edges = data.split(string_to_split_on)[-1]
    # split the data on newline character
    list_of_edges = list_of_edges.split("\n")
    # remove empty strings that arose due to whitespace by using filter
    list_of_edges = list(filter(lambda x: x != "", list_of_edges))

    # create a list of lists of type [from, to] by splitting on the comma character
    list_of_lists_edges = []
    for i in list_of_edges:
        splitted_string = i.split(",")
        # convert the splitted string elements to integer
        sublist_of_edges = [int(i) for i in splitted_string]
        # append the sublist to the major list
        list_of_lists_edges.append(sublist_of_edges)

    return list_of_lists_edges


def parse_number_of_colors(data: str) -> int:
    """Return the given number of colors for graph vertices.
    
    This function will parse the read-in input data looking for the number of colors.

    :param data: read-in input file
    :type data: str
    :return: number of colors
    :rtype: int
    """
    # look for a sequence of digits following the string ''colors = '' with optional spaces until new line
    regex_colors = re.compile("colors\\s?=\\s?([0-9]*)\n")

    # find the matches in data
    num_colors = int(regex_colors.findall(data)[0])

    return num_colors
