import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

# ******** Traditional Merge Sort ********** #
def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge1(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge1(left, right):
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


# ******** Bottom up Merge Sort *********** #
def bottom_up_mergesort(L):
    
    # Subarrays increase by powers of 2: 2^0, 2^1, 2^2, 2^3... 
    # Single elements of 2^0=1 is already sorted
    size = 1   
    n = len(L)                                         
    
    # Continuously iterate while the subarray size is less than the length of the array
    while (size < n):
        
        # Reinitializing left = 0 to always start sorting from the left
        left=0
        
        # Merge while left segment is smaller than the total length of the list
        while (left < n):
            # Middle index of current sub array    
            middle = min( left + size - 1, n-1)
            
            # Right boundary of the subarray being merged
            right = min( left + (size * 2 - 1), n-1)     
            merge2(L, left, middle, right)
            
            # Move to the left boundary of the next subarray
            left = left + (size * 2)
        
        # The conquered subarray size increases by a multiple of 2
        size = size * 2
    return L
   
# Merge items between given bounds
def merge2(L, left, middle, right):
    
    # Size of left segment
    leftSize = middle - left + 1

    # Size of right segment
    rightSize = right - middle
    
    # Creating temporary arrays with 0s
    leftTemp = [0] * leftSize
    rightTemp = [0] * rightSize
    
    # Copy items into the temporary arrays
    for i in range(0, leftSize):
        leftTemp[i] = L[left + i]

    for i in range(0, rightSize):
        rightTemp[i] = L[middle + i + 1]
 
    i, j, k = 0, 0, left

    while j < rightSize and i < leftSize:
        if leftTemp[i] <= rightTemp[j]:
            # Copy items from leftTemp in ascending order
            L[k] = leftTemp[i]
            i += 1
        else:
            # Copy items from rightTemp in ascending order
            L[k] = rightTemp[j]
            j += 1
        k += 1
 
    # Copy remaining elements into merged list
    while i < leftSize:
        L[k] = leftTemp[i]
        i += 1
        k += 1
 
    while j < rightSize:
        L[k] = rightTemp[j]
        j += 1
        k += 1

# ***** Graph Code ***** #

def exp7(n):
    total1 = 0
    total2 = 0
    
    times1 = [] #list of execution time for each list length
    times2 = []
    #list_lengths = [10, 50, 100, 300, 500]
    list_lengths = []
    for i in range(10, 2000, 50):
        list_lengths.append(i)
        for j in range(n):
            L1 = create_random_list(i, 100)
            L2 = L1.copy()

            start = timeit.default_timer()
            mergesort(L1)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            bottom_up_mergesort(L2)
            end = timeit.default_timer()
            total2 += end - start

        times1.append(total1/n)
        times2.append(total2/n)
    print("Traditional Merge Sort: ", total1/n)
    print("Bottom Up Merge Sort: ", total2/n)

    print("Bottom Up Merge Sort takes " + str(total2/total1) + " the amount of time Traditional Merge Sort does.")
    return times1, times2, list_lengths

outputs = exp7(10)
print()
plot.plot(outputs[2], outputs[0], label='Traditional Merge Sort')
plot.plot(outputs[2], outputs[1], label='Bottom Up Merge Sort')
plot.plot()
plot.legend()
plot.title('Execution Times of Sorting Algorithms')
plot.xlabel('List Length')
plot.ylabel('Execution Time (seconds)')
plot.show()