import sys
from collections import deque, Counter

def bestFriendSearch(graph, startWord, endWord):
    if startWord == endWord:
        return 0

    visited = {startWord}
    que = deque([(startWord, 0)])
            
    while que:
        currentNode, dist = que.popleft()
        
        for neighbor in graph[currentNode]:
            if neighbor not in visited:
                if neighbor == endWord:
                    return dist + 1
                    
                visited.add(neighbor)
                que.append((neighbor, dist + 1))
                
    return "Impossible"

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
        
    nWords, nTasks = lines[0].split()
    nWords = int(nWords)
    nTasks = int(nTasks)
    
    words = lines[1:nWords+1]
    
    available_counts = {w: Counter(w) for w in words}
    needed_counts = {w: Counter(w[-4:]) for w in words}
    
    graph = {w: [] for w in words}

    for word in words:
        needed = needed_counts[word]
        
        for otherWord in words:
            if word != otherWord:
                available = available_counts[otherWord]
                
                can_transition = True
                for letter, count in needed.items():
                    if available[letter] < count:
                        can_transition = False
                        break
                
                if can_transition:
                    graph[word].append(otherWord)

    for i in range(nWords+1, nWords+nTasks+1):
        start, target = lines[i].split()
        print(bestFriendSearch(graph, start, target))

if __name__ == '__main__':
    main()

    """
    1. The graph is a dict of words and words it has edges too. We iterate through every combination of words and check if they satisfy the conditions in the problemformulation.
    2. Making key value pairs with avery visited node and their predecessor while we perform the BFS
    3. Time complexity: while loop => maximum of n iterations, for loop maximum of 2m total iterations => O(n + m)
    4. No because DFS is not guaranteed to find the shortest path.
    5. Finding the optimal way to drive between two points, gps navigation, 
    """ 