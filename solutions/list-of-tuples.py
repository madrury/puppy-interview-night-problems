def to_tuple_of_lists(ts: list[tuple[int, int]]) -> tuple[list[int], list[int]]:
    firsts, lasts = [], []
    for fst, lst in ts:
        firsts.append(fst)
        lasts.append(lst)
    return firsts, lasts


def to_list_of_tuples(ts: tuple[list[int], list[int]]) -> list[tuple[int, int]]:
    firsts, lasts = ts
    tups = []
    for fst, lst in zip(firsts, lasts):
        tups.append((fst, lst))
    return tups

def to_filtered_list_of_tuples(ts: tuple[list[int], list[int]]) -> list[tuple[int, int]]:
    firsts, lasts = ts
    tups = []
    for fst, lst in zip(firsts, lasts):
        if (fst + lst) % 2 == 0:
            tups.append((fst, lst))
    return tups

def to_lagged_filtered_list_of_tuples(ts: tuple[list[int], list[int]]) -> list[tuple[int, int]]:
    firsts, lasts = ts
    tups = []
    previous_is_even = False
    for fst, lst in zip(firsts, lasts):
        if previous_is_even:
            tups.append((fst, lst))
        if (fst + lst) % 2 == 0:
            previous_is_even = True
        else:
            previous_is_even = False
    return tups


if __name__ == "__main__":
    assert to_tuple_of_lists([(1, 1), (2, 2), (3, 3)]) == ([1, 2, 3], [1, 2, 3])
    assert to_tuple_of_lists([(1, 1), (1, 2), (1, 3), (1, 4)]) == ([1, 1, 1, 1], [1, 2, 3, 4])
    assert to_tuple_of_lists([(1, 2), (3, 4), (5, 6)]) == ([1, 3, 5], [2, 4, 6])
    assert to_tuple_of_lists([]) == ([], [])

    assert to_list_of_tuples(([1, 2, 3], [1, 2, 3])) == [(1, 1), (2, 2), (3, 3)]
    assert to_list_of_tuples(([1, 1, 1, 1], [1, 2, 3, 4])) == [(1, 1), (1, 2), (1, 3), (1, 4)]
    assert to_list_of_tuples(([1, 3, 5], [2, 4, 6])) == [(1, 2), (3, 4), (5, 6)]
    assert to_list_of_tuples(([], [])) == []

    assert to_filtered_list_of_tuples(([1, 2, 3], [1, 2, 3])) == [(1, 1), (2, 2), (3, 3)]
    assert to_filtered_list_of_tuples(([1, 1, 1, 1], [1, 2, 3, 4])) == [(1, 1), (1, 3)]
    assert to_filtered_list_of_tuples(([1, 3, 5], [2, 4, 6])) == []
    assert to_filtered_list_of_tuples(([], [])) == []

    assert to_lagged_filtered_list_of_tuples(([1, 2, 3], [1, 2, 3])) == [(2, 2), (3, 3)]
    assert to_lagged_filtered_list_of_tuples(([1, 1, 1, 1], [1, 2, 3, 4])) == [(1, 2), (1, 4)]
    assert to_lagged_filtered_list_of_tuples(([1, 3, 5], [2, 4, 6])) == []
    assert to_lagged_filtered_list_of_tuples(([], [])) == []