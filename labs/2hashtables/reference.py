import sys
from collections import deque
from sympy import *

class hashMap():
    def __init__(self):
        self.size = 0
        self.length = 8
        self.alphaUpper = 0.1
        self.buckets = [None] * self.length
        

    def put(self, key,count=1):
        h = hash(key) % self.length
        
        if self.buckets[h] is None:
            self.buckets[h] = deque()
            
        bucket = self.buckets[h]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (k, v + count)
                return
        
        bucket.append((key, count))
        self.size += 1
        self.resize()
    
    def resize(self):
        curAlpha = self.size / self.length
        if curAlpha > self.alphaUpper:
            oldBuckets = self.buckets
            self.length = self.length * 2
            self.buckets = [None] * self.length
            self.size = 0

            for bucket in oldBuckets:
                if bucket is not None:
                    for k, v in bucket:
                        self.put(k, v)   

    def delete(self, key):
        h = hash(key) % self.length
        bucket = self.buckets[h]
        
        if bucket is not None:
            newBucket = deque(pair for pair in bucket if pair[0] != key)
            if len(bucket) != len(newBucket):
                self.size -= 1
            self.buckets[h] = newBucket
    
    def findMax(self):
        max_val = (None, -1)
        for bucket in self.buckets:
            if bucket is not None:
                for k, v in bucket:
                    if v > max_val[1] or (int(v) == max_val[1] and str(k) < max_val[0]):
                        max_val = (k, v)
        return max_val
    
class ProbingHashMap:
    def __init__(self):
        self.size = 0
        self.length = 8
        self.alphaUpper = 0.999
        self.buckets = [None] * self.length
        self.DELETED = object()

    def put(self, key, count=1):
        self.resize()

        i = hash(key) % self.length

        while True:
            cur = self.buckets[i]

            if cur is None:
                self.buckets[i] = (key, count)
                self.size += 1
                return
            elif cur is self.DELETED:
                self.buckets[i] = (key, count)
                self.size += 1
                return
            elif cur[0] == key:
                self.buckets[i] = (key, cur[1] + count)
                return

            else:
                i = (i + 1) % self.length

    def resize(self):
        if self.size / self.length > self.alphaUpper:
            oldBuckets = self.buckets
            self.length = self.length * 2
            self.buckets = [None] * self.length
            self.size = 0

            for bucket in oldBuckets:
                if bucket is not None and bucket is not self.DELETED:
                    self.put(bucket[0], bucket[1])

    def delete(self, key):
        i = hash(key) % self.length

        while True:
            cur = self.buckets[i]
            if cur is None:
                return
            elif cur is self.DELETED:
                i = (i + 1) % self.length
            elif cur[0] == key:
                self.buckets[i] = self.DELETED
                return
            else:
                i = (i + 1) % self.length
    
    def findMax(self):
        max_val = (None, -1)
        for bucket in self.buckets:
            if bucket is not None and bucket is not self.DELETED:
                k, v = bucket
                if v > max_val[1] or (int(v) == max_val[1] and str(k) < max_val[0]):
                    max_val = (k, v)

        return max_val
    
class QuadraticProbingHashMap:
    def __init__(self):
        self.size = 0
        self.length = 13
        self.alphaUpper = 0.1
        self.buckets = [None] * self.length
        self.DELETED = object()

    def put(self, key, count=1):
        self.resize()

        base = hash(key)

        for j in range(self.length):
            i = (base + j * j) % self.length
            cur = self.buckets[i]

            if cur is None:
                self.buckets[i] = (key, count)
                self.size += 1
                return

            elif cur is self.DELETED:
                self.buckets[i] = (key, count)
                self.size += 1
                return

            elif cur[0] == key:
                self.buckets[i] = (key, cur[1] + count)
                return
            
    def resize(self):
        if self.size / self.length > self.alphaUpper:
            oldBuckets = self.buckets
            self.length = nextprime(self.length*2)
            self.buckets = [None] * self.length
            self.size = 0
    
            for bucket in oldBuckets:
                if bucket is not None and bucket is not self.DELETED:
                    self.put(bucket[0], bucket[1])

    def delete(self, key):
        base = hash(key)

        for j in range(self.length):
            i = (base + j * j) % self.length
            cur = self.buckets[i]

            if cur is None:
                return

            elif cur is self.DELETED:
                continue

            elif cur[0] == key:
                self.buckets[i] = self.DELETED
                return 

    def findMax(self):
        max_val = (None, -1)
        for bucket in self.buckets:
            if bucket is not None and bucket is not self.DELETED:
                k, v = bucket
                if v > max_val[1] or (int(v) == max_val[1] and str(k) < max_val[0]):
                    max_val = (k, v)

        return max_val
    





myHash = hashMap()
i = 0
for line in sys.stdin:
    word = line.strip()

    remove_it = i % 16 == 0

    if remove_it:
        myHash.delete(word)
    else:
        myHash.put(word)

    i += 1

ans = myHash.findMax()
print(ans[0], ans[1])

#4. För bra lookup speed är a = ca. 0,75 bra.
#Med seperate chaining kan vi dock ha a > 1
#5. ???
"""
8. Reference 3.3s, Kvadratisk ~8s (a >= 1.0 blir fel), 
linjär ~7,2s (tar ej slut a >= 1.0), Seperate chaining ~8,5s
9. Jag tror att resizingen tar längst tid, gjorde några ändringar i quadratic som tog den från 10 minuter till 8s, vill resiza oftar
10. Bit shift k biter åt vänster då n = 2^k och && 1 på det man får ger modulo n om n är en potens av två.
Märkte ingen riktig ändring"""
