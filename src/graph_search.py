import numpy as np
from .graph import Cell
from .utils import trace_path

"""
General graph search instructions:

First, define the correct data type to keep track of your visited cells
and add the start cell to it. If you need to initialize any properties
of the start cell, do that too.

Next, implement the graph search function. When you find a path, use the
trace_path() function to return a path given the goal cell and the graph. You
must have kept track of the parent of each node correctly and have implemented
the graph.get_parent() function for this to work. If you do not find a path,
return an empty list.

To visualize which cells are visited in the navigation webapp, save each
visited cell in the list in the graph class as follows:
     graph.visited_cells.append(Cell(cell_i, cell_j))
where cell_i and cell_j are the cell indices of the visited cell you want to
visualize.
"""


def depth_first_search(graph, start, goal):
    """Depth First Search (DFS) algorithm. This algorithm is optional for P3.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement DFS (optional)."""

    # If no path was found, return an empty list.
    return []


def breadth_first_search(graph, start, goal):
    """Breadth First Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement BFS."""
    from collections import deque

    queue = deque([start])
    start_node = graph.nodes[start.j][start.i]
    start_node.visited = True
    start_node.distance = 0
    
 
    graph.visited_cells.append(Cell(start.i, start.j))
    
    
    while queue:
        current = queue.popleft()
        current_node = graph.nodes[current.j][current.i]
        
        if current.i == goal.i and current.j == goal.j:
            return trace_path(current, graph)
        
        neighbors = graph.find_neighbors(current.i, current.j)
        for neighbor in neighbors:
            neighbor_node = graph.nodes[neighbor.j][neighbor.i]
     
            if neighbor_node.visited or graph.check_collision(neighbor.i, neighbor.j):
                continue
       
            neighbor_node.visited = True
            neighbor_node.parent = current_node
            neighbor_node.distance = current_node.distance + 1
            
            queue.append(neighbor)
            graph.visited_cells.append(Cell(neighbor.i, neighbor.j))

    return []


def a_star_search(graph, start, goal):
    """A* Search (BFS) algorithm.
    Args:
        graph: The graph class.
        start: Start cell as a Cell object.
        goal: Goal cell as a Cell object.
    """
    graph.init_graph()  # Make sure all the node values are reset.

    """TODO (P3): Implement A*."""

    # If no path was found, return an empty list.
    return []
