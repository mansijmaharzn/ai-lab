def greedy_best_first_search(graph, heuristic, start_node, goal_node):
    visited_nodes = set()
    priority_queue = [(heuristic[start_node], [start_node])]

    while priority_queue:
        (h_value, path) = priority_queue.pop(0)
        current_node = path[-1]

        if current_node == goal_node:
            return path

        visited_nodes.add(current_node)

        for neighbor, distance in graph[current_node].items():
            if neighbor not in visited_nodes:
                new_path = path + [neighbor]
                priority_queue.append((heuristic[neighbor], new_path))

        priority_queue.sort()

    return None


if __name__ == "__main__":
    graph = {
        'S': {'A': 3, 'B': 2},
        'A': {'C': 4, 'D': 1},
        'B': {'E': 3, 'F': 1},
        'C': {},
        'D': {},
        'E': {'H': 5},
        'F': {'I': 2, 'G': 3},
        'G': {},
        'H': {},
        'I': {},
    }

    heuristic = {
        'S': 13,
        'A': 12,
        'B': 4,
        'C': 7,
        'D': 3,
        'E': 8,
        'F': 2,
        'G': 0,
        'H': 4,
        'I': 9,
    }

    print("Greedy Best First Search")
    start_node = input("Enter the start node: ").upper()
    goal_node = input("Enter the goal node: ").upper()

    traversed_path = greedy_best_first_search(graph, heuristic, start_node, goal_node)

    if traversed_path:
        print(f"Goal node found: \n{traversed_path}\n")
    else:
        print("Goal node not found\n")
