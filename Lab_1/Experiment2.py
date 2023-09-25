import timeit
import random
import matplotlib.pyplot as plot

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def insert(L, i):
        print("Current value", L[i])
        current_value = L[i]
        
        while i > 0 and L[i-1] > current_value:
            print("i: ", i)
            L[i] = L[i-1]
            print("Prev num is larger than current value of", current_value, "Shifting one up", L)
            i -= 1
            print("Updated i value: ", i)

        # Only assign current_value once you've found the correct position
        L[i] = current_value
        print("Value before is less. Reached correct position for current value", L)
        
def insertion_sort2(L):
    print("Original List", L)
    for i in range(1, len(L)):
            insert(L, i)
    return L

#L = create_random_list(10, 20)
#print(insertion_sort2(L))


# Optimized Selection Sort

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
            # Search for max value
            if (L[k] > max_value):
                max_index = k
                max_value = L[k]

            # Search for min value
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
        print("Swapped array", L)

def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


L = create_random_list(8, 30)
print("Original array: ", L)
selection_sort2(L)