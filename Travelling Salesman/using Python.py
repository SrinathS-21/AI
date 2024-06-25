from queue import PriorityQueue

def best_first_search(adj_list, heuristics, start):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    path = []

    while not pq.empty():
        cost, node = pq.get()
        if node not in visited:
            path.append((node, cost))
            visited.add(node)
            if len(visited) == len(adj_list):
                return path
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    pq.put((heuristics[neighbor], neighbor))
    return path

if __name__ == "__main__":
    adj_list = {
        'A': ['D', 'C'],
        'B': ['E'],
        'C': ['B', 'E'],
        'D': ['C'],
        'E': ['D', 'A']
    }
    heuristics = {
        'A': 2,
        'B': 5,
        'C': 4,
        'D': 3,
        'E': 6
    }
    start_node = input("Enter start node: ")
    print("\nAdjacency List : ", adj_list)
    print("\nHeuristics : ", heuristics)
    print("\nStarting node = ", start_node)
    print("\nPath followed :")
    path = best_first_search(adj_list, heuristics, start_node)
    total_cost = 0
    for node, cost in path[:-1]:
        total_cost += heuristics[node]
        print(node, "(", cost, ") - Total Cost =", total_cost)
    last_node, last_cost = path[-1]
    total_cost += heuristics[last_node]
    print(last_node, "(", last_cost, ") - Total Cost =", total_cost)
    print(path[0][0])
