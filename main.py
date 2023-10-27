from generate_graph import generate_random_graph
from search_algorythms import breadth_first_search, depth_first_search
from my_animations import search_animation
import pprint

# Variables section
NUMBER_OF_NODES = 50
NUMBER_OF_EDGES_PER_NODE = 4
START_NODE = 5
SEARCH_FOR_NODE = 21
SPEED = 500

# Execution Section
random_graph = generate_random_graph(NUMBER_OF_NODES, NUMBER_OF_EDGES_PER_NODE)
# random_graph2 = generate_random_graph(NUMBER_OF_NODES, NUMBER_OF_EDGES_PER_NODE)

history, back_path = breadth_first_search(START_NODE, random_graph, SEARCH_FOR_NODE)
# history2, back_path2 = breadth_first_search(START_NODE, random_graph2, SEARCH_FOR_NODE)

pprint.pprint(history)

search_animation(random_graph, history, back_path, SPEED)
# search_animation(random_graph2, history2, back_path2)