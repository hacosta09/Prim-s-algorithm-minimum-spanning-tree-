
import heapq

def prim_algorithm(graph, start_vertex):
    """
    Prim's algorithm implementation to find the Minimum Spanning Tree (MST).
    :param graph: Dictionary representation of adjacency list for the graph.
    :param start_vertex: Starting vertex for the algorithm.
    :return: Tuple containing the MST and its total weight.
    """
    mst = []
    total_weight = 0
    visited = set()
    priority_queue = [(0, start_vertex, None)]  # (weight, vertex, parent)

    while priority_queue:
        weight, current_vertex, parent = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        if parent is not None:
            mst.append((parent, current_vertex, weight))
            total_weight += weight

        for neighbor, edge_weight in graph[current_vertex]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (edge_weight, neighbor, current_vertex))

    return mst, total_weight


# Graph representation: adjacency list
# Based on the provided graph
graph = {
    1: [(2, 4), (4, 8)],
    2: [(1, 4), (3, 2), (5, 6)],
    3: [(2, 2), (6, 5)],
    4: [(1, 8), (5, 11), (7, 9)],
    5: [(2, 6), (4, 11), (6, 3), (8, 1)],
    6: [(3, 5), (5, 3), (9, 8)],
    7: [(4, 9), (8, 6)],
    8: [(5, 1), (7, 6), (9, 3)],
    9: [(6, 8), (8, 3)],
}

# Test Prim's algorithm
mst, total_weight = prim_algorithm(graph, start_vertex=1)

print("Minimum Spanning Tree:")
for edge in mst:
    print(f"Edge from {edge[0]} to {edge[1]} with weight {edge[2]}")
print(f"Total weight of MST: {total_weight}")
