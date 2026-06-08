import sys


def find(parent, nod):
    # Folj kedjan av foraldrar tills vi hittar roten (nodens komponent-representant).
    rot = nod
    while parent[rot] != rot:
        rot = parent[rot]
    # Path compression: peka om alla noder pa vagen direkt mot roten,
    # sa att nasta find blir snabbare.
    while parent[nod] != rot:
        parent[nod], nod = rot, parent[nod]
    return rot


def main():
    # Las hela indata pa en gang och dela upp i en lista av heltal.
    data = sys.stdin.buffer.read().split()
    pos = 0

    antal_personer = int(data[pos]); pos += 1
    antal_kanter = int(data[pos]); pos += 1

    # Spara kanterna som (vikt, u, v) sa att sortering sker pa vikten.
    kanter = []
    for _ in range(antal_kanter):
        u = int(data[pos]); pos += 1
        v = int(data[pos]); pos += 1
        vikt = int(data[pos]); pos += 1
        kanter.append((vikt, u, v))

    # Steg 1: sortera kanterna fran lattast till tyngst.
    kanter.sort()

    # Varje nod borjar som sin egen komponent. Noderna ar 1..N.
    parent = list(range(antal_personer + 1))

    total_kostnad = 0

    # Steg 2: ta varje kant om den kopplar samman tva skilda komponenter.
    for vikt, u, v in kanter:
        rot_u = find(parent, u)
        rot_v = find(parent, v)
        if rot_u != rot_v:
            parent[rot_u] = rot_v   # Sla ihop komponenterna.
            total_kostnad += vikt

    print(total_kostnad)


main()