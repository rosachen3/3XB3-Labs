import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

# ******************* Traditional Selection Sort Code *******************
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


# ****************** Optimized Selection Sort Code **********************

def selection_sort2(L):
    i = 0
    j = len(L) - 1
    
    # Run while pointers do not cross each other
    while(i < j):
        max_value = L[i]
        min_value = L[i]
        
        max_index = i
        min_index = i
        
        for k in range(i, j + 1):
            # Search for max value from unsorted part of list
            if (L[k] > max_value):
                max_index = k
                max_value = L[k]

            # Search for min value from unsorted part of list
            elif (L[k] < min_value):
                min_index = k
                min_value = L[k]
          
        # Swapping min to the right position [sorted <here> ..... sorted]
        swap(L,i,min_index)
  
        # Swapping max item to the right position [sorted ....... <here> sorted]
        # If max item was swapped to L[min_index] in previous swap,
        # Swap L[j] and L[min_index]
        if (L[min_index] == max_value):
            swap(L,j,min_index)
        else:
            swap(L,j,max_index)
  
        i += 1
        j -= 1
        # print("Swapped array", L)

# ****************** Graph for Selection Sort **********************

def compareSelectionRunTimes(n):
    total1 = 0
    total2 = 0
    times1 = [] #list of execution time for each list length
    times2 = []
    list_lengths = []

    for i in range(10, 1000, 50):
        list_lengths.append(i)
        for j in range(n):
            L = create_random_list(i, 100)
            start = timeit.default_timer()
            selection_sort(L)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            selection_sort2(L)
            end = timeit.default_timer()
            total2 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
    print("Traditional Insertion Sort: ", total1/n)
    print("Optimized Insertion Sort: ", total2/n)
    return times1, times2, list_lengths

outputs2 = compareSelectionRunTimes(10)
print()
plot.plot(outputs2[2], outputs2[0], label='Traditional Selection Sort')
plot.plot(outputs2[2], outputs2[1], label='Optimized Selection Sort')
plot.plot()
plot.legend()
plot.title('Running Time of Traditional Selection Sort Vs Optimized Selection Sort ')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()