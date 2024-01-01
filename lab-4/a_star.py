def astar_search(graph, heuristic_values, start_node, goal_node):
    open_nodes = {start_node}
    closed_nodes = set()
    g_scores = {start_node: 0}
    parents = {start_node: start_node}

    def get_neighbors(node):
        return graph[node]

    def heuristic_estimate(node):
        return heuristic_values[node]

    while open_nodes:
        current_node = min(open_nodes, key=lambda x: g_scores[x] + heuristic_estimate(x))

        if current_node == goal_node:
            reconstructed_path = []
            while parents[current_node] != current_node:
                reconstructed_path.append(current_node)
                current_node = parents[current_node]
            reconstructed_path.append(start_node)
            reconstructed_path.reverse()

            print(f'Path found: {reconstructed_path}')
            return reconstructed_path

        for (neighbor, weight) in get_neighbors(current_node):
            if neighbor not in open_nodes and neighbor not in closed_nodes:
                open_nodes.add(neighbor)
                parents[neighbor] = current_node
                g_scores[neighbor] = g_scores[current_node] + weight
            elif g_scores[neighbor] > g_scores[current_node] + weight:
                g_scores[neighbor] = g_scores[current_node] + weight
                parents[neighbor] = current_node
                if neighbor in closed_nodes:
                    closed_nodes.remove(neighbor)
                    open_nodes.add(neighbor)
        open_nodes.remove(current_node)
        closed_nodes.add(current_node)

    print('Path does not exist!')
    return None


if __name__ == "__main__":
    graph = {
        'A': [('B', 2), ('C', 1)],
        'B': [('D', 5)],
        'C': [('D', 3), ('E', 4)],
        'D': [('E', 2)],
        'E': []
    }

    heuristic_values = {
        'A': 3,
        'B': 4,
        'C': 2,
        'D': 6,
        'E': 0
    }

    start_node = input("Enter the start node: ").upper()
    goal_node = input("Enter the goal node: ").upper()

    astar_search(graph, heuristic_values, start_node, goal_node)
