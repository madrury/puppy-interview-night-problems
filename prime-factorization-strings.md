## Prime Factor Strings
This exercise covers a common task in everyday programming: extracting data from a string of text.

### Parsing
A text file contains many strings that give the prime factorization of *positive* integers:

```
The prime factors of 16 are 2, 2, 2, 2
The prime factors of 12 are 2, 2, 3
The prime factor of 227 is 227
The prime factors of 154 are 2, 7, 11
```

Write a function that parses one of these strings into a pair of the number and a list of its prime factors:

```python
parse_prime_factor_string(s: str) -> Tuple[int, List[int]]
    ...
```

In our examples:

```python
parse_prime_factor_string("The prime factors of 16 are 2, 2, 2, 2")
(16, [2, 2, 2, 2])
parse_prime_factor_string("The prime factors of 12 are 2, 2, 3")
(12, [2, 2, 3])
parse_prime_factor_string("The prime factor of 227 is 227")
(227, [227])
parse_prime_factor_string("The prime factors of 154 are 2, 7, 11")
(154, [2, 7, 11])
```

### The Number is Missing
It turns out some of the lines in the text file are corrupted! In these, the product number itself is missing and replaced with a `?`:

```
The prime factors of 16 are 2, 2, 2, 2
The prime factors of ? are 2, 2, 3
The prime factor of 227 is 227
The prime factors of ? are 2, 7, 11
```

Your task is the same, only now you'll need to infer the number if needed:

```python
parse_prime_factor_string_product_missing("The prime factors of 16 are 2, 2, 2, 2")
(16, [2, 2, 2, 2])
parse_prime_factor_string_product_missing("The prime factors of ? are 2, 2, 3")
(12, [2, 2, 3])
parse_prime_factor_string_product_missing("The prime factor of 227 is 227")
(227, [227])
parse_prime_factor_string_product_missing("The prime factors of ? are 2, 7, 11")
(154, [2, 7, 11])
```

###  Exactly One Number is Missing
It's worse than you thought! *All* the lines are corrupted, but at least in a predictable way: in every line *exactly one* of the numbers in the string is missing, it may be the product number itself, or one of the prime factors. Your task is the same, but you'll need to infer the missing number:

```python
parse_prime_factor_string_something_missing("The prime factors of 16 are 2, ?, 2, 2")
(16, [2, 2, 2, 2])
parse_prime_factor_string_something_missing("The prime factors of 12 are 2, 2, ?")
(12, [2, 2, 3])
parse_prime_factor_string_something_missing("The prime factor of 227 is ?")
(227, [227])
parse_prime_factor_string_something_missing("The prime factors of ? are 2, 7, 11")
(154, [2, 7, 11])
```