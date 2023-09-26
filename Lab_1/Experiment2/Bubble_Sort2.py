import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Traditional Bubble sort code *******************

def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Optimized Bubble sort code *******************

def bubble_sort2(L):
    for j in range(len(L)-1):
        i = 0
        while i < len(L)-i-1:
            i += 1
            if L[i] < L[i-1]: # if the number before is bigger, set it as n
                n = L[i-1] # storing value that we are sorting
                L[i-1] = L[i]
                i += 1
                while i < len(L) and L[i] < n: # compare the following numbers with n
                    L[i-1] = L[i]
                    i += 1
                L[i-1] = n # placing n at the correct position

# ****************** Graph for Bubble Sort **********************
def compareInsertionRunTimes(n):
    total1 = 0
    total2 = 0
    times1 = [] #list of execution time for each list length
    times2 = []
    list_lengths = []

    for i in range(10, 1000, 50):
        list_lengths.append(i)
        for j in range(n):
            L = create_random_list(i, 100)
            L2 = L.copy()
            start = timeit.default_timer()
            bubble_sort(L)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            bubble_sort2(L2)
            end = timeit.default_timer()
            total2 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
    print("Traditional Bubble Sort: ", total1/n)
    print("Optimized Bubble Sort: ", total2/n)
    return times1, times2, list_lengths

outputs1 = compareInsertionRunTimes(10)
print()
plot.plot(outputs1[2], outputs1[0], label='Traditional Bubble Sort')
plot.plot(outputs1[2], outputs1[1], label='Optimized Bubble Sort')
plot.plot()
plot.legend()
plot.title('Running Time of Traditional Bubble Sort Vs Optimized Bubble Sort ')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()