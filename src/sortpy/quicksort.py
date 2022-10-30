from typing import List, Any


def quicksort(la: List[Any]) -> List[Any]:
    if la == []:
        return []

    pivot, *rest = la

    low = [x for x in rest if x < pivot]
    equal = [x for x in rest if x == pivot]
    high = [x for x in rest if x > pivot]

    return quicksort(low) + [pivot] + equal + quicksort(high)
