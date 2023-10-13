import networkx as nx
import matplotlib.pyplot as plt
import random

# Graph generation section
def generate_random_graph(number_of_nodes, spread):
    random_graph = nx.Graph()
    stack= []
    nodes = [i for i in range(number_of_nodes-1, -1, -1)]
    current_node = 0
    base_node = nodes.pop()

    stack.append(base_node)
    random_graph.add_node(base_node)

    while len(nodes):
        r = random.randrange(spread - 1) + 2
        base_node = stack.pop(0)

        while r>0 and len(nodes):
            current_node = nodes.pop()
            stack.append(current_node)

            random_graph.add_node(current_node)
            random_graph.add_edge(base_node, current_node)

            r -= 1
    return random_graph

random_graph = generate_random_graph(60, 8)

# Drawing section
nx.draw(random_graph, with_labels=True, node_size=200, node_color='lightblue', font_size=8)
plt.title("Random Graph")
plt.show()
