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
            if items[i - 1] > j:
                bu[i][j] = bu[i - 1][j]
            else:
                bu[i][j] = max(bu[i-1][j], bu[i-1][j-items[i - 1][0]] + items[i - 1][1])
    return bu[len(items)][capacity]

def ks_top_down(items: List[Tuple[int,int]], capacity: int) -> int:
    return 0

def top_down_aux(items, i, j, td):
    if i == 0 or j == 0:
        td[(i, j)] = 0
    else:
        if items[i - 1][0] > j:
            if not (i - 1, j) in td:
                td[(i, j)] = top_down_aux(items, i - 1, j, td)
        else:
            td[(i, j)] = max(top_down_aux(items, i - 1, j, td), top_down_aux(items, i - 1, j - items[i - 1][0], td) + items[i - 1][1])
    return td[(i, j)]
#### TESTING CODE ####
# ks_brute_force(randItemSet(10, 2, 17, 100, 200), 20)
# ks_rec(randItemSet(4, 2, 17, 100, 200), 20)
ks_top_down(randItemSet(4, 2, 17, 100, 200), 20)
######################

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

outputs = Exp1(100)

plot.plot(outputs[2], outputs[0], label='brute force imp.')
plot.plot(outputs[2], outputs[1], label='recursive imp.')

plot.plot()
plot.legend()
plot.title('Runtime vs. Number of Items for ks implementations')
plot.xlabel('Number of Items')
plot.ylabel('Runtime (s)')
plot.show()