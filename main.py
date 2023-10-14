import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
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
        r = random.randrange(spread) + 1
        base_node = stack.pop(0)

        while r>0 and len(nodes):
            current_node = nodes.pop()
            stack.append(current_node)

            random_graph.add_node(current_node)
            random_graph.add_edge(base_node, current_node)

            r -= 1
    return random_graph

random_graph = generate_random_graph(80, 4)



# Animation section

def BFS(graph, node):
    # TODO: change 0 to first element of given graph
    stack = [[0, x] for x in list(graph.neighbors(0))]
    visited = [0] 
    print('visited: ', visited)
    print("stack: ", stack)
    
# From this moment [1] index means value of node, and [0] index means the previous node
    while len(stack):
        x = stack.pop(0)
        visited.append(x[1])
        print('visited appended: ', visited)
        if node in list(graph.neighbors(x[1])):
           visited.append(node)
           print('value found')
           break
        stack.extend([[x[1], y] for y in list(graph.neighbors(x[1]))])
        print("stack extended: ", stack)
        stack.remove([x[1], x[0]])


        print('visited: ', visited)
        print("stack: ", stack)
    
    return visited

visited = BFS(random_graph, 79)


pos = nx.spring_layout(random_graph)
fig, ax = plt.subplots()
node_colors = {node: 'gray' for node in random_graph.nodes}

def update(frame):
    ax.clear()
    node_colors[visited[frame]] = 'pink'
    if frame == len(visited)-1: node_colors[visited[frame]] = 'red'

    nx.draw(random_graph, pos, with_labels=True, node_size=200, node_color=[node_colors[node] for node in random_graph.nodes], font_size=8)
    plt.title(f'{frame}')
    
ani = FuncAnimation(fig, update, frames=range(len(visited)), repeat=False, blit=False, interval=100)

plt.show()