import matplotlib.pyplot as plt
from P3 import NaivePriorityQueue, HeapPriorityQueue, PythonHeapPriorityQueue, timeit

ns_lst = [10, 20, 50, 100, 200, 500]
naive_time = timeit(pqclass = NaivePriorityQueue)
heap_time = timeit(pqclass = HeapPriorityQueue)
py_h_time = timeit(pqclass = PythonHeapPriorityQueue)

plt.figure(figsize = (10, 7))
plt.plot(ns_lst, naive_time, label="Naive Priority Queue")
plt.plot(ns_lst, heap_time, label="Heap Priority Queue")
plt.plot(ns_lst, py_h_time, label='Python Heap Priority Queue')
plt.xlabel('Number of Lists Merged')
plt.ylabel('Elapsed time in seconds')
plt.title('Comparison Amongst Three Types of Priority Queue Implementations')
plt.legend()
plt.show(block = True)
plt.savefig('P3-C.png')

