import sys
def main ():
    data = sys.stdin.read().split('\n') #läser in data, varje element en rad
    pos = 0

    chars = data[pos].split()
    pos += 1
    k = len(chars) #nbr items

    char_to_index = {c: i for i, c in enumerate(chars)}

    cost = []
    for _ in range(k):
        cost.append(list(map(int, data[pos].split())))
        pos += 1

    Q = int(data[pos])
    pos += 1

    queries = []
    for _ in range (Q):
        s1, s2 = data[pos].split()
        queries.append((s1, s2))
        pos += 1
    
    out = []
    for s1, s2 in queries:
        F = align(s1, s2, cost, char_to_index)
        a1, a2 = backtrack(s1, s2, F, cost, char_to_index)
        out.append(f"{a1} {a2}")
    print('\n'.join(out))
    

GAP = -4
#DP
def align(s1, s2, cost, char_to_index):
    n = len(s1)
    m = len(s2)

    #n och m är längder på de två strängarna
    #F[i][j] = bästa poäng för s1[i] mot s2[i]
    F = [[0] * (m+1) for _ in range (n + 1)] #0 är den tomma prefixen

    #basfall: tom sträng mot j tecken = j gap
    for i in range (1, n+1):
        F[i][0] = i * GAP
    for j in range(1, m + 1):
        F[0][j] = j * GAP

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a = char_to_index[s1[i - 1]]
            b = char_to_index[s2[j - 1]]

            diagonal = F[i - 1][j - 1] + cost[a][b] #aligna s1 mot s2
            up = F[i - 1][j] + GAP
            left = F[i][j - 1] + GAP

            F[i][j] = max(diagonal, up, left)

    return F

def backtrack(s1, s2, F, cost, char_to_index):
    i = len(s1)
    j = len(s2)
    out1 = []
    out2 = []

    while i > 0 or j > 0:
        if i > 0 and j > 0:
            a = char_to_index[s1[i - 1]]
            b = char_to_index[s2[j - 1]]
            if F[i][j] == F[i - 1][j - 1] + cost[a][b]:
                # diagonal : båda tecken alignear
                out1.append(s1[i - 1])
                out2.append(s2[j - 1])
                i -= 1
                j -= 1
                continue

        if i > 0 and F[i][j] == F[i - 1][j] + GAP:
            #uppåt
            out1.append(s1[i - 1])
            out2.append('*')
            i -= 1
        else: 
            #vänster
            out1.append('*')
            out2.append(s2[j - 1])
            j -= 1
    
    out1.reverse()
    out2.reverse()
    return ''.join(out1), ''.join(out2)

main()




