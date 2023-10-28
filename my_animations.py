import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D

# Animation Section 
def search_animation(graph, hist, bp, speed, seed, title, geometry):
    # graph - graph that we want to animate
    # hist - history of steps from search algorythm
    # bp (backwards-path) - path from node that we were looking for to base node of graph
    # speed - time of interval in ms

    pos = nx.spring_layout(graph, seed = seed)
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)
    fig.canvas.manager.window.geometry(geometry)
    node_colors = {node: 'lightgray' for node in graph.nodes}

    visited = [0]
    stack = [0]
    unvisited = [0]

    def update(frame):
        ax.clear()
        if frame >= len(hist):
            if(bp == [None]):
                plt.title(f'Finished in {len(hist)} steps\nNode not found')
            else:
                node_colors[bp[frame-len(hist)]] = 'purple'
                plt.title(f'Finished in {len(hist)} steps\nDistance: {len(bp)-1}')

            legend_labels = [unvisited[0], stack[0], visited[0]]
            legend_colors = ['lightgray', 'gray', 'red']
        else:    
            node_colors[hist[frame]['current']] = 'red'
            try:
                for x in hist[frame]['tbv']:
                    node_colors[x[1]] = 'gray'
            except:
                pass
            plt.title(f'Step: {frame}')
        
            visited[0] = "Visited: " + str(hist[frame]['visited'])
            stack[0] = "Queue: " + str(hist[frame]['stack'])
            unvisited[0] = "Unvisited: " + str(graph.number_of_nodes() - hist[frame]['stack'] - hist[frame]['visited'])

            legend_labels = [unvisited[0], stack[0], visited[0]]
            legend_colors = ['lightgray', 'gray', 'red']
            
        legend_handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for color, label in zip(legend_colors, legend_labels)]
        ax.legend(handles=legend_handles, labels=legend_labels, title='State of nodes', loc='upper right')

        nx.draw(graph, pos, with_labels=True, node_size=200, node_color=[node_colors[node] for node in graph.nodes], font_size=8)
    
    animation = FuncAnimation(fig, update, frames=len(hist)+len(bp), repeat=False, blit=False, interval=speed)
    
    plt.show()