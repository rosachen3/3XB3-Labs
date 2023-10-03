from math import log
import math
import timeit
import random
import matplotlib.pyplot as plot

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************

def exp5(n):
    times1 = [] #list of execution time for each list length
    times2 = []
    times3 = []
    #swapValues = [0, 20, 40, 60, 80, 100, 120]

    swapValues = []
    length = 700
    for swaps in range(0, 2100, 100):
        total1 = 0
        total2 = 0
        total3 = 0
        #for i in swapValues:  
        swapValues.append(swaps)
        for j in range(n):
            L1 = create_near_sorted_list(length, 700, swaps)
            L2 = L1.copy()
            L3 = L1.copy()
            #L.sort()

            start = timeit.default_timer()
            quicksort(L1)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            mergesort(L2)
            end = timeit.default_timer()
            total2 += end - start

            start = timeit.default_timer()
            heapsort(L3)
            end = timeit.default_timer()
            total3 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
        times3.append(total3/n)
    print("Quick Sort: ", total1/n)
    print("Merge Sort: ", total2/n)
    print("Heap Sort: ", total3/n)
    print("Merge Sort takes " + str(total2/total1) + " the amount of time Quick Sort does.")
    print("Heap Sort takes " + str(total3/total1) + " the amount of time Quick Sort does.")
    print("Merge Sort takes " + str(total2/total3) + " the amount of time Heap Sort does.")
    return times1, times2, times3, swapValues

outputs = exp5(20)
print()
plot.plot(outputs[3], outputs[0], label='Quick Sort')
plot.plot(outputs[3], outputs[1], label='Merge Sort')
plot.plot(outputs[3], outputs[2], label='Heap Sort')
plot.plot()
plot.legend()
plot.title('Swaps vs. Runtime')
plot.xlabel('Swaps')
plot.ylabel('Execution Time (seconds)')
plot.show()