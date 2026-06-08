import sys
from collections import deque, Counter

#Counter räknar antal förekomster av bokstav i ord 
def can_go(word, other): #Får man gå från ett ord till ett annat
    needed = Counter(word[-4:]) #De 4 sista bokstäverna av A ska finnas i B
    available = Counter(other) #Dessa bokstäver finns

    for letter in needed:
        if available[letter] < needed[letter]: #Om antalet av en bokstav som finns är mindre
            return False 

    return True



def BFS(start: str, end: str, connections: dict):
    visited = {start}
    queue = deque([start]) #De vi ska besöka näst (BFS)
    distance = {start: 0} #Ord från start, räkna kortaste

    while queue:
        current = queue.popleft() #älsta ordet först (BFS)

        if current == end:
            return distance[current]

        for word in connections[current]:
            if word not in visited: #Om granne ej besökts
                visited.add(word)
                queue.append(word)
                distance[word] = distance[current] + 1

    return "Impossible"



def solve():
    #with open('data/secret/2small2.in', 'r', encoding='utf-8') as file:
        #ines_list = [line.strip() for line in file] #Läser rad för rad (lista av str)
    lines_list = [line.strip() for line in sys.stdin]

    words = [] #två listor
    paths = []

    N, Q = lines_list[0].split() #"4 2" -> "4" "2"
    N = int(N) #antal ord
    Q = int(Q) #antal frågor (vad ska vi testa)

    for i in range(1, N + 1):
        words.append(lines_list[i]) #hämtar raden på i

    for i in range(N + 1, N + Q + 1): #se hur data är utformad
        paths.append(lines_list[i])

    connections = {} #k = ord, V = lista på alla ord man får gå till från det ordet

    for word in words: #flr varje ird skapas nyckel i connections med tom lista
        connections[word] = []

    for word in words:
        for other_word in words:
            if other_word != word and can_go(word, other_word):
                connections[word].append(other_word)

    for path in paths:
        start, end = path.split()
        print(BFS(start, end, connections))


solve()