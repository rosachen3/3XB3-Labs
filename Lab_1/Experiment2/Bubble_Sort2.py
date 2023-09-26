# When inserting a value via insertion sort, you are essentially “bubbling down” the value into the sorted portion. 
# Therefore, the optimization you made to insertion sort, can also be applied to bubble sort. 
# This will be slightly more complicated since in bubble sort you will need to potentially insert many values and 
# shift things appropriately during a single iteration. Name this implementation of Bubble Sort bubble_sort2(). 

import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def bubble_sort2(L, i = 0):
    print("original list: ", L)
    for j in range(len(L)-1):
        i = 0
        while i < len(L)-1:
            i += 1
            if L[i] < L[i-1]:
                n = L[i-1] # storing value that we are sorting
                L[i-1] = L[i]
                i += 1
                while i < len(L) and L[i] < n:
                    L[i-1] = L[i]
                    i += 1
                L[i-1] = n
        print("list after ", j+1, "round of sorting", L)
L = create_random_list(10, 20)
bubble_sort2(L)