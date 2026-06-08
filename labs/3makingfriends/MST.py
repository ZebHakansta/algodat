import sys


def find(parent, node):
    root = node
    while parent[root] != root: 
        root = parent[root]# Klättra uppåt tills vi når en nod som pekar på sig själv      # = det är roten
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

#1. VI kör kruskals algoritm (sorterar och hittar alla noder som inte redan är sammankopplade). Använder vår find-funktion för att hitta roten
#2. O(M log M), det är sorteringen som tar mest tid, de andra delarna är linjära 
#3. Nätet blir inte helt ihopkopplat llängre, du måste hitta den nya billigaste kopplingen mellan noderna. Finns bara EN väg mellan varje i MST, i verkligheten vill man ha alternativ
#4. Ex. elnät. Du vill koppla samman ALLA stolpar, du vill minimera kostnad
