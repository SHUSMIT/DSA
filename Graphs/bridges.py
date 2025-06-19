def dfs(node, parent, time_insertion, lowest_time, visited, bridges, timer, adjL):
    visited[node] = True
    time_insertion[node] = lowest_time[node] = timer
    timer += 1

    for neighbour in adjL[node]:
        if neighbour == parent:
            continue  # skip if its parent
        if not visited[neighbour]:
            dfs(neighbour, node, time_insertion, lowest_time, visited, bridges, timer, adjL)
            lowest_time[node] = min(lowest_time[node], lowest_time[neighbour]) ## backtrack

            if lowest_time[neighbour] > time_insertion[node]:
                bridges.append((node, neighbour))  # it's a bridge
        else:
            # visited neighbour, borrow its time
            lowest_time[node] = min(lowest_time[node], time_insertion[neighbour])


def find_bridges(edges, V):
    adjL = {i: [] for i in range(V)}
    for (u, v) in edges:
        adjL[u].append(v)
        adjL[v].append(u)

    time_insertion = [-1] * V
    lowest_time = [-1] * V
    visited = [False] * V
    bridges = []
    timer = 0

    for i in range(V):
        if not visited[i]:
            dfs(i, -1, time_insertion, lowest_time, visited, bridges, timer, adjL)

    return bridges
