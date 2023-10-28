import multiprocessing
from generate_graph import generate_random_graph
from search_algorythms import breadth_first_search, depth_first_search
from my_animations import search_animation

# Variables section
NUMBER_OF_NODES = 50
NUMBER_OF_EDGES_PER_NODE = 4
START_NODE = 5
SEARCH_FOR_NODE = 30
SPEED = 100
SEED = 10

assert isinstance(NUMBER_OF_NODES, int) and NUMBER_OF_NODES > 0, "NUMBER_OF_NODES has to be intiger greater than 0"
assert isinstance(NUMBER_OF_EDGES_PER_NODE, int) and NUMBER_OF_EDGES_PER_NODE > 0, "NUMBER_OF_EDGES_PER_NODE has to be intiger greater than 0"
assert isinstance(START_NODE, int) and START_NODE >= 0, "START_NODE has to be intiger greater or equal 0"
assert isinstance(SEARCH_FOR_NODE, int) and SEARCH_FOR_NODE >= 0, "SEARCH_FOR_NODE has to be intiger greater or equal 0"
assert isinstance(SPEED, int) and SPEED > 0, "SPEED has to be intiger greater than 0"
assert isinstance(SEED, int) and SEED >= 0, "SEED has to be intiger greater or equal 0"

# Execution Section
random_graph = generate_random_graph(NUMBER_OF_NODES, NUMBER_OF_EDGES_PER_NODE, SEED)

history_bfs, back_path_bfs = breadth_first_search(START_NODE, random_graph, SEARCH_FOR_NODE)
history_dfs, back_path_dfs = depth_first_search(START_NODE, random_graph, SEARCH_FOR_NODE)

def animate_bfs():
    search_animation(random_graph, history_bfs, back_path_bfs, SPEED, SEED, "Breadth First Search (BFS)", "-0+0")

def animate_dfs():
    search_animation(random_graph, history_dfs, back_path_dfs, SPEED, SEED, "Depth First Search (DFS)", "+0+0")

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = animate_bfs)
    p2 = multiprocessing.Process(target = animate_dfs)

    p1.start()
    p2.start()