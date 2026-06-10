import math
from collections import defaultdict, deque


def bfs(graph, drain):
    visited = {0}
    queue = deque([(0, math.inf, [])])

    while queue:
        current_node, flow, path = queue.popleft()

        for edge_index, (child, capacity, _) in enumerate(graph[current_node]):
            if capacity <= 0 or child in visited:
                continue

            current_flow = min(flow, capacity)
            new_path = path + [(current_node, edge_index)]

            if child == drain:
                return new_path, current_flow

            visited.add(child)
            queue.append((child, current_flow, new_path))

    return None, 0


def edmund_karp(graph, drain):
    flow = 0

    while True:
        path, max_flow = bfs(graph, drain)

        if path is None:
            return flow

        flow += max_flow

        for node, edge_index in path:
            v, vw, reverse_index = graph[node][edge_index]
            _, uw, _ = graph[v][reverse_index]

            graph[node][edge_index] = (v, vw - max_flow, reverse_index)
            graph[v][reverse_index] = (node, uw + max_flow, edge_index)


def main():
    node_count, edge_count, min_flow, plan_size = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(edge_count)]
    removal_plan = [int(input()) for _ in range(plan_size)]

    graph = defaultdict(list)
    for u, v, w in edges:
        # (dst, weight, reverse index)
        graph[u].append((v, w, len(graph[v])))
        graph[v].append((u, w, len(graph[u]) - 1))

    flow = edmund_karp(graph, node_count - 1)
    removed = 0

    left = 0
    right = plan_size - 1

    while left <= right:
        mid = left + (right - left) // 2

        edges_to_remove = {edges[r] for r in removal_plan[:mid]}

        graph = defaultdict(list)
        for edge in edges:
            if edge in edges_to_remove:
                continue

            u, v, w = edge
            graph[u].append((v, w, len(graph[v])))
            graph[v].append((u, w, len(graph[u]) - 1))

        # print(f"{i + 1}/{plan_size}")

        new_flow = edmund_karp(graph, node_count - 1)
        if new_flow >= min_flow:
            removed = mid
            flow = new_flow
            left = mid + 1
        else:
            right = mid - 1

    print(removed, flow)


if __name__ == "__main__":
    main()
"""
Tidskomplexitet O(n e^2): varje kant kan vara en flaskhals max en gång för varje nod i grafen, ifall vi tex har en väldigt sammankopplad graf vilket ger O(nE) sedan är BFS O(E). Vi kan också behöva ta bort C kanter i det här fallet vilket ger en tidskomplexitet närmare O(CnE^2)
Bipartit matchning, para ihop arbetare med uppgifter
Kolla på de kanter med högst vikt först och sedan minska tröskeln allt eftersom 
"""