"""minheaop 
adjencey list
träd algoritm"""

# Open the file in read mode ('r')
import heapq
import random


def Janik(graph, first):
    MST = []
    visited = set()
    totWeight = 0
    heap = [(0, None, first)]
    
    while heap:
        weight, source, dest = heapq.heappop(heap)

        if dest in visited:
            continue
            
        visited.add(dest)

        if not source is None:
            MST.append((source, dest, weight))
            totWeight += weight 
        
        for weight, newDest in graph[dest]:
            if newDest not in visited:
                heapq.heappush(heap, (weight, dest, newDest))
    return totWeight

    
    

def main():
    first = True
    attending = 0
    nPairs = 0
    graph = {}
    with open('labs/3makingfriends/data/secret/3large.in', 'r', encoding='utf-8') as file:
        for line in file:
            # .strip() removes trailing newlines (\n) and extra whitespace
            print(line.strip())
            if first:
                attending, nPairs = line.split()
                first = False
            else:
                source, destination, weight = line.split()
                weight = int(weight)
                if source in graph:
                    graph[source].append((weight, destination))
                else:
                    graph.update({source : [(weight, destination)]})
                if destination in graph:
                    graph[destination].append((weight, source))
                else:
                    graph.update({destination : [(weight, source)]})



    first = random.choice(list(graph.keys()))
    print(graph)
    print(Janik(graph, first))


if __name__ == "__main__":
    main()




        