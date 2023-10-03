import timeit
import random
import matplotlib.pyplot as plot


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

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


# # ************ Dual Quick Sort ************ 
def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    if L[0] > L[len(L)-1]:
        L[0] = L[len(L)-1]
        L[len(L)-1] = L[0]
    pivot1 = L[0]
    pivot2 = L[len(L) - 1]
    left, middle, right= [], [], []
    # iterate through list L starting at index 1
    for num in L[1:]:
        if num < pivot1:
            left.append(num)
        elif num > pivot2:
            right.append(num)
        else:
            middle.append(num)
    return dual_quicksort_copy(left) + [pivot1] + dual_quicksort_copy(middle) + [pivot2] + dual_quicksort_copy(right)

# ************************************* 


# ************ Timing Function ************
def exp6(n):
    times1 = [] #list of execution time for each list length
    times2 = []
    #list_lengths = [10, 50, 100, 300, 500]
    list_lengths = []
    for i in range(0, 2100, 100):
        total1 = 0
        total2 = 0
        list_lengths.append(i)
        for j in range(n):
            L1 = create_random_list(i, 100)
            L2 = L1.copy()

            start = timeit.default_timer()
            quicksort(L1)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            dual_quicksort(L2)
            end = timeit.default_timer()
            total2 += end - start
        times1.append(total1/n)
        times2.append(total2/n)
    print("Traditional Quicksort: ", total1/n)
    print("Dual Quicksort: ", total2/n)
    print("Dual Quicksort takes " + str(total2/total1) + " times the amount of time Traditional Quicksort takes.")
    return times1, times2, list_lengths

outputs = exp6(20)
print()
plot.plot(outputs[2], outputs[0], label='Dual Quicksort')
plot.plot(outputs[2], outputs[1], label='Traditional Quicksort')
plot.plot()
plot.legend()
plot.title('Execution Times of Traditional Quicksort vs. Dual Quicksort')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()