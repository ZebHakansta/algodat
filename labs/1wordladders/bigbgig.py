import sys
from collections import deque, Counter


def can_go(word, other):
    needed = Counter(word[-4:])
    available = Counter(other)

    for letter in needed:
        if available[letter] < needed[letter]:
            return False

    return True


def BFS(s: str, t: str, connections: dict):
    visited = {s}
    queue = deque([s])
    distance = {s: 0}

    while queue:
        current = queue.popleft()

        if current == t:
            return distance[current]

        for word in connections[current]:
            if word not in visited:
                visited.add(word)
                queue.append(word)
                distance[word] = distance[current] + 1

    return "Impossible"


def solve():
    with open('data/secret/3medium1.in', 'r', encoding='utf-8') as file:
        lines_list = [line.strip() for line in file]

    words = []
    paths = []

    N, Q = lines_list[0].split()
    N = int(N)
    Q = int(Q)

    for i in range(1, N + 1):
        words.append(lines_list[i])

    for i in range(N + 1, N + Q + 1):
        paths.append(lines_list[i])

    connections = {}

    for word in words:
        connections[word] = []

    for word in words:
        for itWord in words:
            if itWord != word and can_go(word, itWord):
                connections[word].append(itWord)

    for path in paths:
        start, end = path.split()
        print(BFS(start, end, connections))


solve()