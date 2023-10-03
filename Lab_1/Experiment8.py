from math import log
import timeit
import random
import matplotlib.pyplot as plot

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return
# *************************************


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


# ************ Timing Function ************
def exp4(n):
    times1 = [] #list of execution time for each list length
    times2 = []
    times3 = []
    #list_lengths = [10, 50, 100, 300, 500]
    list_lengths = []
    for i in range(0, 400, 50):
        total1 = 0
        total2 = 0
        total3 = 0
        list_lengths.append(i)
        for j in range(n):
            L1 = create_random_list(i, 3000)
            L2 = L1.copy()
            L3 = L1.copy()

            start = timeit.default_timer()
            insertion_sort(L1)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            quicksort(L2)
            end = timeit.default_timer()
            total2 += end - start

            start = timeit.default_timer()
            mergesort(L3)
            end = timeit.default_timer()
            total3 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
        times3.append(total3/n)
    return times1, times2, times3, list_lengths

outputs = exp4(20)
print()
plot.plot(outputs[3], outputs[0], label='Insertion Sort')
plot.plot(outputs[3], outputs[1], label='Quicksort')
plot.plot(outputs[3], outputs[2], label='Mergesort')
plot.plot()
plot.legend()
plot.title('List Length vs. Execution Time (seconds)')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()

# ************************************* 