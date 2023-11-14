import random
from itertools import chain, combinations
import timeit
from typing import List, Tuple
import matplotlib.pyplot as plot


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
    subSets = list(chain.from_iterable(combinations(items, r) for r in range(len(items) + 1)))
    for i in subSets:
        sumWeight = 0
        sumValue = 0
        for j in i:
            sumWeight += j[0]
            sumValue += j[1]
        if sumWeight <= capacity:
            if sumValue > highestValue:
                highestValue = sumValue
    return highestValue

def ks_rec(items: List[Tuple[int,int]], capacity: int) -> int:
    if not items or capacity == 0:
        return 0
    notIncluding_i = ks_rec(items[:-1],capacity)
    including_i = ks_rec(items[:-1], capacity-items[len(items) - 1][0]) + items[len(items) - 1][1]
    return max(notIncluding_i, including_i)

def ks_bottom_up(items: List[Tuple[int,int]], capacity: int) -> int:
    bu = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if items[i - 1][1] > j:
                bu[i][j] = bu[i - 1][j]
            else:
                bu[i][j] = max(bu[i-1][j], bu[i-1][j-items[i - 1][0]] + items[i - 1][1])
    return bu[len(items)][capacity]
    
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


def Exp1(n):
    ks_brute_force_runtime = []
    ks_rec_runtime = []
    num_of_items = []

    for items in range(1, 20, 2):
    # for edges in edge_values:
        total1 = 0
        total2 = 0
        num_of_items.append(items)
        set = randItemSet(items, 50, 200, 1000, 2000)
        for j in range(n):
            start = timeit.default_timer()
            ks_brute_force(set, 100)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            ks_rec(set, 100)
            end = timeit.default_timer()
            total2 += end - start
        ks_brute_force_runtime.append(total1/n)
        ks_rec_runtime.append(total2/n)
      
    return ks_brute_force_runtime, ks_rec_runtime, num_of_items

# outputs = Exp1(100)

# plot.plot(outputs[2], outputs[0], label='brute force imp.')
# plot.plot(outputs[2], outputs[1], label='recursive imp.')

# plot.plot()
# plot.legend()
# plot.title('Runtime vs. Number of Items for ks implementations')
# plot.xlabel('Number of Items')
# plot.ylabel('Runtime (s)')
# plot.show()


def Exp2(n):
    ks_bottom_up_runtime = []
    ks_top_down_runtime = []
    num_of_items = []

    for items in range(1, 20, 2):
    # for edges in edge_values:
        total1 = 0
        total2 = 0
        num_of_items.append(items)
        # set = randItemSet(items, 50, 200, 1000, 2000)
        set = randItemSet(items, 50, 75, 50, 75)
        for j in range(n):
            start = timeit.default_timer()
            ks_bottom_up(set, 100)
            end = timeit.default_timer()
            total1 += end - start

            start = timeit.default_timer()
            ks_top_down(set, 100)
            end = timeit.default_timer()
            total2 += end - start
        ks_bottom_up_runtime.append(total1/n)
        ks_top_down_runtime.append(total2/n)
      
    return ks_bottom_up_runtime, ks_top_down_runtime, num_of_items

outputs = Exp2(100)

plot.plot(outputs[2], outputs[0], label='bottom up imp.')
plot.plot(outputs[2], outputs[1], label='top down imp.')

plot.plot()
plot.legend()
plot.title('Runtime vs. Number of Items for ks implementations BP vs. TD')
plot.xlabel('Number of Items')
plot.ylabel('Runtime (s)')
plot.show()

