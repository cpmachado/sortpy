from sortpy import mergesort


def test_sorted():
    a = [x for x in range(10)]

    assert a == mergesort(a)
    assert [] == mergesort([])


def test_reversed():
    a = [9 - x for x in range(10)]

    assert [x for x in range(10)] == mergesort(a)
