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

L = create_random_list(10, 20)
print(insertion_sort2(L))