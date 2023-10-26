import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Animation Section 
def search_animation(graph, hist, bp, SPEED):

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