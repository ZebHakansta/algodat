import sys


def find(parent, node):
    root = node
    while parent[root] != root:
        root = parent[root]
    while parent[node] != root:
        parent[node], node = root, parent[node]
    return root


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0

    amount_people = int(data[pos]); pos += 1
    amount_edges = int(data[pos]); pos += 1

    edges = []
    for _ in range(amount_edges):
        u = int(data[pos]); pos += 1
        v = int(data[pos]); pos += 1
        weight = int(data[pos]); pos += 1
        edges.append((weight, u, v))

    edges.sort()
    parent = list(range(amount_people + 1))

    total_cost = 0

    for weight, u, v in edges:
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v  
            total_cost += weight

    print(total_cost)


main()