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