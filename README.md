# Algorithmic-Puzzle-Solver

## Overview
This Python project is a grid-based pathfinding visualizer built using `pygame`. Users can select a grid size and choose between multiple search algorithms to navigate from the start position (top-left) to the goal position (bottom-right). The program supports:

- **Breadth-First Search (BFS)**
- **Hill Climbing Search**
- **A* Search**
- **Genetic Algorithm (GA) Search**

## Features
- Interactive grid selection (5x5, 7x7, 9x9, 11x11, 31x31)
- Multiple search algorithms for pathfinding
- Visualization of search paths
- Comparison of BFS and A* performance
- Genetic Algorithm optimization for search

## Installation
Before running the script, ensure you have Python installed along with the required dependencies:

```sh
pip install pygame numpy
```

## Usage
Run the script using:

```sh
python script.py
```

### Grid Selection
Upon execution, you will be prompted to select a grid size using the keyboard:
- `a` - 5x5 grid
- `b` - 7x7 grid
- `c` - 9x9 grid
- `d` - 11x11 grid
- `e` - 31x31 grid (for large-scale visualization)

### Search Algorithm Selection
After selecting the grid, choose a search algorithm:
- `a` - Breadth-First Search (BFS)
- `b` - Hill Climbing Search
- `c` - A* Search
- `d` - Genetic Algorithm
- `e` - Compare BFS and A*

### Large Grid Mode (31x31)
For large grids, only A* Search and BFS are available:
- `a` - A* Search
- `b` - BFS

### Genetic Algorithm Mode
If the Genetic Algorithm is selected, another prompt allows you to choose:
- `a` - A* Search for GA evaluation
- `b` - BFS for GA evaluation

## Controls
- **`SPACE`**: Displays the computed path solution.
- **`ESC`**: Exits the program.

## Search Algorithms Explained
### Breadth-First Search (BFS)
A classic unweighted graph search algorithm that explores nodes layer by layer until the goal is found.

### Hill Climbing Search
A heuristic-based search that iteratively improves the grid by selecting paths that reduce the distance to the goal.

### A* Search
An informed search algorithm using a heuristic (Euclidean distance) to determine the optimal path.

### Genetic Algorithm (GA)
An evolutionary approach that applies crossover and mutation to generate better paths over multiple iterations.

## Example Output
The program renders the grid and visualizes the path found by the chosen algorithm. If no path is found, it displays `NO PATH` in red.

## Dependencies
- `pygame` (for visualization)
- `numpy` (for grid management and numerical operations)
