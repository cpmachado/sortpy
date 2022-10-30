from sortpy.quicksort import quicksort


def test_sorted():
    a = [x for x in range(10)]

    assert a == quicksort(a)
    assert [] == quicksort([])


def test_reversed():
    a = [9 - x for x in range(10)]

    assert [x for x in range(10)] == quicksort(a)
