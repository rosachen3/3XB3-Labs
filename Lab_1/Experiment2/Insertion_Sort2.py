import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Traditional Insertion Sort Code *******************

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

# ****************** Optimized Insertion Sort Code **********************

def insert2(L, i):
        current_value = L[i]
        
        while i > 0 and L[i-1] > current_value:
            L[i] = L[i-1]
            i -= 1

        L[i] = current_value
        return L
        
def insertion_sort2(L):
    # print(L)
    for i in range(1, len(L)):
            insert2(L, i)
            # print(L)
    return L

# L = create_random_list(7, 20)
# print(insertion_sort2(L))

# ****************** Graph for Insertion Sort **********************
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
            insertion_sort(L)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            insertion_sort2(L2)
            end = timeit.default_timer()
            total2 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
    print("Traditional Insertion Sort: ", total1/n)
    print("Optimized Insertion Sort: ", total2/n)
    return times1, times2, list_lengths

outputs1 = compareInsertionRunTimes(10)
print()
plot.plot(outputs1[2], outputs1[0], label='Traditional Insertion Sort')
plot.plot(outputs1[2], outputs1[1], label='Optimized Insertion Sort')
plot.plot()
plot.legend()
plot.title('Running Time of Traditional Insertion Sort Vs Optimized Insertion Sort ')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()