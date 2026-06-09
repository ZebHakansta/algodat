import math
import sys


def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def bruteForce(points):
    d = math.inf
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            curDist = dist(points[i], points[j])
            if curDist < d:
                d = curDist
    return d



def closestPair(X, Y):
    n = len(X)

    if len(X) <= 3:
        return bruteForce(X)
    mid = n // 2
    mid_point = X[mid]

    Py_left = []
    Py_right = []
    for p in Y:
        if p[0] <= mid_point[0]:
            Py_left.append(p)
        else:
            Py_right.append(p)


    dL = closestPair(X[:mid], Py_left)
    dR = closestPair(X[mid:], Py_right)

    d = min(dL, dR)
    strip = [p for p in Y if abs(p[0] - mid_point[0]) < d]

    strip_len = len(strip)
    for i in range(strip_len):
        for j in range(i + 1, strip_len):
            if (strip[j][1] - strip[i][1]) >= d:
                break 
            d = min(d, dist(strip[i], strip[j]))

    return d




def main():
    lines = sys.stdin.read().splitlines()
    nLines = int(lines[0])
    points = []
    for i in range(1, nLines + 1):
        x, y = map(float, lines[i].split())
        points.append((int(x), int(y)))
    xSort = sorted(points, key=lambda p: p[0])
    ySort = sorted(points, key=lambda p: p[1])

    print(f"{closestPair(xSort, ySort):.6f}")

main()

"""
1. Tidscomplexiteten är O(nlog(n)) eftersom det är tidskomplexiteten av att sortera listan med punkter och ingen del av algoritmen överstiger den.
2. För att två punkter som är längre än delta från varandra i y-led inte kan vara närmare än delta.
3. Se bild
4. Vid basfallen 1, 2, 3 punkter i en spalt.
Brute force is O(n^2) while this is O(n log(n))
"""



