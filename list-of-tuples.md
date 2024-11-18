## List of Tuples and Tuple of Lists
This exercise covers a straightforward case of an essential skill in everyday programming: take data that looks like this and make it look like that.

### Forward
Write a function to convert a `List[Tuple[int, int]]` into a `Tuple[List[int], List[int]]`, where, in the second datatype, the lists are constrained to have the same length.

```python
to_tuple_of_lists(ts: List[Tuple[int, int]]) -> Tuple[List[int], List[int]]:
    ...
```

Some examples:

```python
to_tuple_of_lists([(1, 1), (2, 2), (3, 3)])
([1, 2, 3], [1, 2, 3])
to_tuple_of_lists([(1, 1), (1, 2), (1, 3), (1, 4)])
([1, 1, 1, 1], [1, 2, 3, 4])
to_tuple_of_lists([(1, 2), (3, 4), (5, 6)])
([1, 3, 5], [2, 4, 5])
to_tuple_of_lists([])
([], [])
```

### Backwards
Write the inverse function: convert a `Tuple[List[int], List[int]]` into a `List[Tuple[int, int]]`, where, in the first datatype, the lists are constrained to have the same length.

```python
to_list_of_tuples(ts: Tuple[List[int], List[int]]) -> List[Tuple[int, int]])
    ...
```

Examples are the reverese of the first set:

```python
to_list_of_tuples([1, 2, 3], [1, 2, 3])
[(1, 1), (2, 2), (3, 3)]
to_list_of_tuples([1, 1, 1, 1], [1, 2, 3, 4])
[(1, 1), (1, 2), (1, 3), (1, 4)]
to_list_of_tuples([1, 3, 5], [2, 4, 5])
[(1, 2), (3, 4), (5, 6)]
to_list_of_tuples([], [])
[]
```

### Filtering
Modify your `to_list_of_tuples` function to apply a filter: only include a tuple the the final list when the sum of its entries is divisible by 2:

```python
to_filtered_list_of_tuples([1, 2, 3], [1, 2, 3])
[(1, 1), (2, 2), (3, 3)]
to_filtered_list_of_tuples([1, 1, 1, 1], [1, 2, 3, 4])
[(1, 1), (1, 3)]
to_filtered_list_of_tuples([1, 3, 5], [2, 4, 6])
[]
to_filtered_list_of_tuples([], [])
[]
```

### Lagged Filtering
Modify your `to_filtered_list_of_tuples` to apply a lagged filter: include a tuple when and only when the sum of the entries of the *previous* tuple is even:

```python
to_lagged_filtered_list_of_tuples([1, 2, 3], [1, 2, 3])
[(2, 2), (3, 3)]
to_lagged_filtered_list_of_tuples([1, 1, 1, 1], [1, 2, 3, 4])
[(1, 2), (1, 4)]
to_filtered_list_of_tuples([1, 3, 5], [2, 4, 6])
[]
to_filtered_list_of_tuples([], [])
[]
```