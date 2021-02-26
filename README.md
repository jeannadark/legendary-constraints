# Graph Coloring - Constraint Satisfaction Problem

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#how-it-works">How It Works</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The goal of this project is to color a given graph's vertices with a given number of colors, so that no two adjacent vertices are of the same color.

<!-- USAGE EXAMPLES -->
## Usage

To run this code, one argument is taken from the command line: file name.

Example of how to run the program (located in folder ``csp_search``):
``` sh
    runner.py
```
This will prompt the user to input the file name they want to parse.

If the file is not found, the default `inputs/colors.txt` in this directory is used instead.

Any inputted file should follow the same format as the default to enable accurate parsing of graph data.

## How It Works

1. module ``runner.py`` contains the function ``runner()`` that parses the data, constructs the graph and the CSP problem, and finally, finds the color assignment solution. The solution is then printed to the console.
2. module ``input_reader.py`` contains such functions as ``parse_edges()``and ``parse_number_of_colors()`` that read the input file in the appropriate format.
3. module ``grapher.py``contains the undirected unweighted graph class ``UGraph`` that constructs the graph by using the parsed graph edge data.
4. module ``csp.py`` contains the ``CSP`` class that handles color assignments and generates constraints for a classic CSP problem.
5. module ``ac3.py`` implements the classic AC3 arc-consistency algorithm to check the consistency of the color assignments.
6. module ``backtrack.py`` performs the backtracking search by picking up the most constrained vertex from the list of unassigned vertices and trying to assign the least constraining color to it, if the assignment is consistent.
7. modules ``csp_utils.py`` and ``heuristics.py`` contain MRV, LCV heuristics algorithms and their helper functions.
