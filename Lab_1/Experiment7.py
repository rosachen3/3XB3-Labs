import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

# Iterative merge 
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
            merge(L, left, middle, right)
            
            # Move to the left boundary of the next subarray
            left = left + (size * 2)
        
        # The conquered subarray size increases by a multiple of 2
        size = size * 2
    return L
   
# Merge items between given bounds
def merge(L, left, middle, right):
    
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

L = create_random_list(10, 100)
bottom_up_mergesort(L)

