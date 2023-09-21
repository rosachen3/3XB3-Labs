"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import timeit
import random
import matplotlib.pyplot as plot


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
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


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

def exp1(n):
    total1 = 0
    total2 = 0
    total3 = 0
    times1 = [] #list of execution time for each list length
    times2 = []
    times3 = []
    #list_lengths = [10, 50, 100, 300, 500]
    list_lengths = []
    for i in range(10, 1000, 50):
        list_lengths.append(i)
        for j in range(n):
            L = create_random_list(i, 100)
            #L.sort()

            start = timeit.default_timer()
            insertion_sort(L)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            total2 += end - start

            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            total3 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
        times3.append(total3/n)
    print("Insertion Sort: ", total1/n)
    print("Bubble Sort: ", total2/n)
    print("Selection Sort: ", total3/n)
    print("Bubble Sort takes " + str(total2/total1) + " the amount of time Insertion Sort does.")
    print("Selection Sort takes " + str(total3/total1) + " the amount of time Insertion Sort does.")
    print("Bubble Sort takes " + str(total2/total3) + " the amount of time Selection Sort does.")
    return times1, times2, times3, list_lengths

outputs = exp1(10)
print()
plot.plot(outputs[3], outputs[0], label='Insertion Sort')
plot.plot(outputs[3], outputs[1], label='Bubble Sort')
plot.plot(outputs[3], outputs[2], label='Selection Sort')
plot.plot()
plot.legend()
plot.title('Execution Times of Sorting Algorithms')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()