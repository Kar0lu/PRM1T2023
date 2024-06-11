# Comparison of Graph Search Algorithms
## Project Objective
The goal of the project is to illustrate and compare the following graph search algorithms:
- Depth-first search (DFS)
- Breadth-first search (BFS)
## Requirements
```
matplotlib==3.7.1
networkx==3.1
```
## Creating a Virtual Environment
### Windows
```
python -m venv myenv
myenv\Scripts\activate
pip install matplotlib==3.7.1 networkx==3.1
```
### Linux/ macOS
```
python -m venv myenv
source myenv/bin/activate
pip install matplotlib==3.7.1 networkx==3.1
```
## Method of Comparison
The program creates an animation illustrating the operation of the above algorithms on a (pseudo)randomly generated graph. The animation steps through the algorithm, coloring the appropriate nodes depending on what is currently happening to them. Additionally, the following information is presented on the chart:
- number of undiscovered nodes
- number of nodes on the stack (to be discovered)
- number of discovered nodes
- algorithm step (in how many steps the sought element was found)
- distance of the sought node from the start node
## Comparison
<table width="100%" >
  <thead>
    <tr>
      <th width="20%"></th>
      <th width="40%">Depth-first search (DFS)</th>
      <th width="40%">Breadth-first search (BFS)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td width="20%">Animation</td>
      <td width="40%"><img src="https://github.com/Kar0lu/PP/blob/main/dfs.gif"/></td>
      <td width="40%"><img src="https://github.com/Kar0lu/PP/blob/main/bfs.gif"/></td>
    </tr>
    <tr>
      <td width="20%">Time complexity (V - number of nodes, E - number of edges)</td>
      <td width="40%">O(V + E)</td>
      <td width="40%">O(V + E)</td>
    </tr>
    <tr>
      <td width="20%">Space complexity (V - number of nodes, E - number of edges, H - length of the longest simple path)</td>
      <td width="40%">O(H)</td>
      <td width="40%">O(V + E) - if the input graph is represented by an adjacency list, O(V^2) - if the input graph is represented by an adjacency matrix</td>
    </tr>
    <tr>
      <td width="20%">Completeness</td>
      <td width="40%">Only for finite graphs (without loops)</td>
      <td width="40%">Complete</td>
    </tr>
  </tbody>
</table>

## Detailed Description
It is worth noting that the presented program is not only for finding the sought elements in the graph, so it contains a lot of code that would be redundant if we were only concerned with efficiency. It stores information about the steps of the algorithms and what happens to the various lists during their execution.
### The program contains 3 auxiliary modules:
<details>
<summary>generate_graph.py</summary>
  <br/>This module contains a function generating a (pseudo)random graph. It has no loops.<br/><br/>

  **Input data:**
  
  - number of nodes
  - maximum number of outgoing edges from one node
  - seed

  **Output data:**

  - (pseudo)random graph

</details>
<details>
<summary>search_algorithms.py</summary>
  <br/>This module contains two graph search functions (BFS and DFS)<br/><br/>
  
  **Input data:**
  
  - graph
  - sought node
  - start node

  **Output data:**

  - record of the steps of the used algorithm
  - return path from the end node to the start node

</details>
<details>
<summary>my_animations.py</summary>
  
  <br/>This module contains a function drawing the graph and creating an animation using libraries such as networkx and matplotlib.<br/>
  
  **Input data:**
  
  - graph
  - record of the steps of the used algorithm
  - return path from the end node to the start node
  - animation speed

  **Output data:**

  - none

</details>

### The program is executed through main.py, which works as follows:
<ol>
  <li>
    Declares and validates global constants:
  </li><br/>
  <ul>
    <li>number of nodes in the graph</li>
    <li>maximum number of new branches from one node</li>
    <li>start node</li>
    <li>sought node</li>
    <li>animation speed</li>
    <li>seed</li>
  </ul><br/>
  <li>Generates a random graph</li>
  <li>Searches the graph using the available functions, then receives from them a record of the algorithm's operation step by step, and the return path from the sought node to the start, if the node was found</li>
  <li>Creates an animation based on the record of the algorithm's operation</li>
  <li>Displays the user the animation of the operation of the DFS and BFS algorithms on the same graph and at the same time</li>
</ol>

## Literature
- https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=lbp
- https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=lbp
- https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
