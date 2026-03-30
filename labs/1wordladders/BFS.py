with open('labs/1wordladders/data/secret/1small1.in', 'r') as file:
    # Get the first line and split it into N and Q
    first_line = file.readline().split()
    n = int(first_line[0])
    q = int(first_line[1])

    # Read the next N lines for words
    G = []
    for _ in range(n):
        G.append(file.readline().strip()) # .strip() removes the '\n'

    # Read the next Q lines for queries
    for _ in range(q):
        start, end = file.readline().split()
        # Call your BFS function here
        # result = bfs(start, end)
        # print(result)

print(n, q, G)

#s and t are the endpoints
#G is the list

def BFS(G, s, t):
    print("Hej")


