import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import pprint

# Variables section
NUMBER_OF_NODES = 50
NUMBER_OF_EDGES_PER_NODE = 4
START_NODE = 5
SEARCH_FOR_NODE = 21
SPEED = 100

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
        r = random.randrange(spread) + 1
        base_node = stack.pop(0)

        while r>0 and len(nodes):
            current_node = nodes.pop()
            stack.append(current_node)

            random_graph.add_node(current_node)
            random_graph.add_edge(base_node, current_node)

            r -= 1
    return random_graph

# Search section
def backwards_search(visited):
    finish = visited[0][1]
    next = visited[-1][0]
    ps = [visited[-1][1], next]

    for x in visited[::-1]:
        if(x[1] == next):
            next = x[0]
            ps.append(next)
            if(next == finish):
                break

    return ps

def breadth_first_search(start, graph, search):
    # stack[n] = [visited node, to be visited node]
    # visited[n] = [previous node, visited node]

    stack = [[None, start]]
    visited = []
    step = 0
    history = {}

    # print('visited: ', visited)
    # print("stack: ", stack)
    # print('\n')
    
    while len(stack):
        current = stack.pop(0)
        visited.append(current)
        if current[1] == search:
            history[step] = {
                'current': current[1]
            }
            break
        tbv = [[current[1], x] for x in list(graph.neighbors(current[1]))]
        try:
            tbv.remove([current[1], current[0]])
        except ValueError:
            pass
        stack.extend(tbv)
        history[step] = {
            'current': current[1],
            'tbv': tbv
        }
        step += 1

        # print('current: ', current)
        # print('visited: ', visited)
        # print("stack: ", stack)
        # print('\n')

    # print('current: ', current)
    # pprint.pprint(visited)
    # print("stack: ", stack)
    # pprint.pprint(history)
    # print('\n')

    back_path = backwards_search(visited)
    # print('BP: ', back_path)
    return history, back_path

# Animation Section 
def search_animation(graph, hist, bp):

    pos = nx.spring_layout(graph)
    fig, ax = plt.subplots()
    node_colors = {node: 'lightgray' for node in graph.nodes}

    def update(frame):
        ax.clear()
        if frame >= len(hist):
            node_colors[bp[frame-len(hist)]] = 'purple'
            plt.title(f'{len(hist)}')
        else:    
            node_colors[hist[frame]['current']] = 'red'
            try:
                for x in hist[frame]['tbv']:
                    node_colors[x[1]] = 'gray'
            except:
                pass
            plt.title(f'{frame}')
        nx.draw(graph, pos, with_labels=True, node_size=200, node_color=[node_colors[node] for node in graph.nodes], font_size=8)

    animation = FuncAnimation(fig, update, frames=len(hist)+len(bp), repeat=False, blit=False, interval=SPEED)

    plt.show()

# Execution Section
random_graph = generate_random_graph(NUMBER_OF_NODES, NUMBER_OF_EDGES_PER_NODE)
# random_graph2 = generate_random_graph(NUMBER_OF_NODES, NUMBER_OF_EDGES_PER_NODE)

history, back_path = breadth_first_search(START_NODE, random_graph, SEARCH_FOR_NODE)
# history2, back_path2 = breadth_first_search(START_NODE, random_graph2, SEARCH_FOR_NODE)

search_animation(random_graph, history, back_path)
# search_animation(random_graph2, history2, back_path2)