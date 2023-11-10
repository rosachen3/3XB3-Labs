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
    
    return 0
def ks_bottom_up(items: List[Tuple[int,int]], capacity: int) -> int:

    return 0
def ks_top_down(items: List[Tuple[int,int]], capacity: int) -> int:

    return 0

#### TESTING CODE ####
# ks_brute_force(randItemSet(10, 2, 17, 100, 200), 20)