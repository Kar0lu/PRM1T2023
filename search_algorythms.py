# Search section
def backwards_search(visited):
    # visited - stack of visited nodes
    # bp (backwards_path) - array with path from node that we were looking for to base node of graph

    finish = visited[0][1]
    next = visited[-1][0]
    bp = [visited[-1][1], next]

    for x in visited[::-1]:
        if(x[1] == next):
            next = x[0]
            bp.append(next)
            if(next == finish):
                break

    return bp

def breadth_first_search(start, graph, search):
    # start - node to start
    # graph - graph that we're searching
    # search - node to find

    # stack - stack of nodes that algorythm will check
    # visited - stack nodes that algorythm checked
    # step - variable to store information about steps of algorythm, used in history
    # history - dictionary with information about algorythm on every step

    stack = [[None, start]]
    visited = []
    step = 0
    history = {}
    
    while len(stack):
        current = stack.pop(0)
        visited.append(current)
        if current[1] == search:
            history[step] = {
                'current': current[1],
                'tbv': [],
                'stack': len(stack),
                'visited': len(visited)
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
            'tbv': tbv,
            'stack': len(stack),
            'visited': len(visited)
        }
        step += 1

    back_path = backwards_search(visited)

    return history, back_path



def depth_first_search(start, graph, search):
    # start - node to start
    # graph - graph that we're searching
    # search - node to find
    
    # stack - stack of nodes that algorythm will check
    # visited - stack nodes that algorythm checked
    # step - variable to store information about steps of algorythm, used in history
    # history - dictionary with information about algorythm on every step

    stack = [[None, start]]
    visited = []
    step = 0
    history = {}
    
    while len(stack):
        current = stack.pop(0)
        visited.append(current)
        if current[1] == search:
            history[step] = {
                'current': current[1],
                'tbv': [],
                'stack': len(stack),
                'visited': len(visited)
            }
            break
        tbv = [[current[1], x] for x in list(graph.neighbors(current[1]))]
        try:
            tbv.remove([current[1], current[0]])
        except ValueError:
            pass
        stack[:0] = tbv
        history[step] = {
            'current': current[1],
            'tbv': tbv,
            'stack': len(stack),
            'visited': len(visited)
        }
        step += 1

    back_path = backwards_search(visited)

    return history, back_path