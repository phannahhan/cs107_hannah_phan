from random import sample
from time import time
from P2 import *
import heapq


class PriorityQueue:
    def __init__(self, max_size):
        self.elements = []
        self.max_size = max_size

    def __len__(self):
        return len(self.elements)

    def __bool__(self):
        return len(self.elements) > 0

    def put(self, val):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError
        

def mergesortedlists(lists, pqclass=PriorityQueue):
    merged = []
    pq = pqclass(len(lists))
    for i, l in enumerate(lists): 
        pq.put((l.pop(0), i))

    while pq:
        ele, i = pq.get()
        merged.append(ele)
        if lists[i]:
            pq.put((lists[i].pop(0), i)) 

    return merged


def generatelists(n, length=20, dictionary_path='words.txt'):
    with open(dictionary_path, 'r') as f:
        words = [w.strip() for w in f.readlines()]
    lists = []
    for _ in range(n):
        lists.append(sorted(sample(words, length)))
    return lists


def timeit(ns=(10, 20, 50, 100, 200, 500), pqclass=PriorityQueue, n_average=5):
    elapsed = []
    for n in ns:
        timeaccum = 0
        for _ in range(n_average):
            lists = generatelists(n)
            start = time()
            merged = mergesortedlists(lists, pqclass)
            end = time()
            timeaccum += end - start
        elapsed.append(timeaccum / n_average)
    return elapsed


class NaivePriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        
    def put(self, val):
        if len(self.elements) >= self.max_size:
            raise IndexError('Max Size For Priority Queue Has Been Reached')
        self.elements.append(val)

    def get(self):
        if len(self.elements) == 0:
            raise IndexError('Empty Priority Queue')

        val = self.peek()
        self.elements.remove(val)
        return val

    def peek(self):
        if len(self.elements) == 0:
            raise IndexError('Empty Priority Queue')
        return min(self.elements)


class HeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        #self.max_size = max_size
        #self.elements = MinHeap([])
        super().__init__(max_size)
        self.heap = MinHeap(self.elements)
        
    def put(self, val):
        if len(self) >= self.max_size:
            raise IndexError("Max Size of Priority Queue Has Been Reached")
        self.heap.heappush(val)

    def get(self):
        if len(self) == 0:
            raise IndexError('Empty Priority Queue')
        return self.heap.heappop()

    def peek(self):
        if len(self) == 0:
            raise IndexError('Empty Priority Queue')
        return self.heap.elements[0]


class PythonHeapPriorityQueue(PriorityQueue):
    def __init__(self, max_size):
        super().__init__(max_size)
        self.heapq = self.elements
        heapq.heapify(self.heapq)

    def put(self, val):
        if len(self) == self.max_size:
            raise IndexError("Max Size of Priority Queue Has Been Reached 9")
        heapq.heappush(self.heapq, val)

    def get(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return heapq.heappop(self.heapq)

    def peek(self):
        if len(self) == 0:
            raise IndexError("Empty Priority Queue")
        return self.heapq[0]

# Part A Demo
# q = NaivePriorityQueue(2)
# q.put(1)
# q.put(2)
# print(q.peek())

# 1

# print(q.get())
# 1
# print(q.get())
# 2

