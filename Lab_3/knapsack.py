import random
from itertools import chain, combinations
from typing import List, Tuple

def randItemSet(numOfItems: int, minWeight: int, maxWeight: int, minValue: int, maxValue: int) -> List[Tuple[int,int]]:
    #Generate a list of items within specifed weight, and value ranges
    randItemSet = []
    for i in range(numOfItems):
        weight = random.randint(minWeight, maxWeight)
        value = random.randint(minValue, maxValue)
        randItemSet.append((weight, value))
    return randItemSet


def ks_brute_force(items: List[Tuple[int,int]], capacity: int) -> int:
    highestValue = 0
    print("Set of Items: ", items)
    subSets = list(chain.from_iterable(combinations(items, r) for r in range(len(items) + 1)))
    print("All possible sets: ", subSets)
    for i in subSets:
        sumWeight = 0
        sumValue = 0
        for j in i:
            sumWeight += j[0]
            sumValue += j[1]
        if sumWeight <= capacity:
            if sumValue > highestValue:
                highestValue = sumValue
    print("highest value is: ", highestValue)
    return highestValue

def ks_rec(items: List[Tuple[int,int]], capacity: int) -> int:
    if not items or capacity == 0:
        return 0
    notIncluding_i = ks_rec(items[:-1],capacity)
    including_i = ks_rec(items[:-1], capacity-items[len(items) - 1][0]) + items[len(items) - 1][1]
    return max(notIncluding_i, including_i)

def ks_bottom_up(items: List[Tuple[int,int]], capacity: int) -> int:
    n = len(items)
    # Create a 2D list with dimensions [capacity][# of items]
    # Initialize array with -1s
    K = []
    for i in range(n+1):
        row = []
        for j in range(capacity+1):
            row.append(0)
        K.append(row)

    # Fill in table using bottom up approach 
    for i in range(n+1):
        for j in range(capacity+1):
            # Base case: If there are no items or the weight is 0, the max value is 0
            if i == 0 or j == 0:
                K[i][j] = 0
            # The weight of the current item is less than the current capacity
            elif items[i-1][0] <= j:
                K[i][j] = max(K[i-1][j], items[i-1][1] + K[i-1][j-items[i-1][0]])
            # Weight of current item is larger than current capacity
            # The value is set to be the same as the one from the row above 
            else: 
                K[i][j] = K[i-1][j]
    return K[n][capacity]

    
def ks_top_down(items: List[Tuple[int,int]], capacity: int) -> int:
    n = len(items)
    # Initialize array with -1s
    K = []
    for i in range(n+1):
        row = []
        for j in range(capacity+1):
            row.append(-1)
        K.append(row)

    # Helper function for recursive top-down approach
    def top_down(capacity, n):
        # Base case: No items or capacity is 0, value is always 0
        if n == 0 or capacity == 0:
            return 0
        # Weight of current item us <= capacity left
        if items[n-1][0] <= capacity:
            # Take the max value b/w including current element or not
            K[n][capacity] = max(
                items[n-1][1] + top_down(capacity - items[n-1][0], n-1),
                top_down(capacity, n-1)
            )
            return K[n][capacity]
        
        # Weight of current item > capacity
        else:
            K[n][capacity] = top_down(capacity, n-1)
            return K[n][capacity]

    return top_down(capacity, n)

    

    

#### TESTING CODE ####
# ks_brute_force(randItemSet(10, 2, 17, 100, 200), 20)
# ks_rec(randItemSet(4, 2, 17, 100, 200), 20)

# items = [(1,1),(3,4),(4,5),(5,7)]
# capacity = 7
# results = ks_top_down(items, capacity)
# print("Maximum value is ", results)