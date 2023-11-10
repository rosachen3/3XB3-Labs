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
    
    return 0
def ks_rec(items: List[Tuple[int,int]], capacity: int) -> int:
    
    return 0
def ks_bottom_up(items: List[Tuple[int,int]], capacity: int) -> int:

    return 0
def ks_top_down(items: List[Tuple[int,int]], capacity: int) -> int:

    return 0

