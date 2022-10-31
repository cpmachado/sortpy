from typing import List, Any


def merge(left: List[Any], right: List[Any]) -> List[Any]:
    result = []

    while left and right:
        if left[0] <= right[0]:
            x, *left = left
            result.append(x)
        else:
            x, *right = right
            result.append(x)

    while left:
        x, *left = left
        result.append(x)

    while right:
        x, *right = right
        result.append(x)

    return result


def mergesort(m: List[Any]) -> List[Any]:
    m_len = len(m)
    if m_len <= 1:
        return m

    mid = m_len // 2

    left = m[:mid]
    right = m[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)
