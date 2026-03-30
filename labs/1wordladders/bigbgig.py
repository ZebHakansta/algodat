import sys

def solve():
    with open('labs/1wordladders/data/sample/1.in', 'r', encoding='utf-8') as file:
    # .strip() removes the \n at the end of each line
        lines_list = [line.strip() for line in file]

    words = []
    paths = []

    N, Q = lines_list[0].split()
    N = int(N)
    Q = int(Q)
    for i in range(1, N):
        words.append(lines_list[i])

    for i in range(N+1, N + Q):
        paths.append(lines_list[i])

    connections = {}

    for word in words:
        for itWord in words:
            if itWord != word and set(word[-4:].lower()).issubset(set(itWord.lower())):
                if word not in connections:
                    connections[word] = [itWord]  # Initialize the list if the key is new
                    
                connections[word].append(itWord)
    print(connections)
                


solve()