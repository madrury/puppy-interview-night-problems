def parse_prime_factor_string(s: str) -> tuple[int, list[int]]:
    words: list[str] = s.split(' ')
    cleaned = [w.strip(' ,') for w in words]
    digits = [int(w) for w in cleaned if w.isdigit()]
    return (digits[0], digits[1:])


def parse_prime_factor_string_product_missing(s: str) -> tuple[int, list[int]]:
    words: list[str] = s.split(' ')
    cleaned = [w.strip(' ,') for w in words]
    digits = [w for w in cleaned if (w.isdigit() or w == '?')]
    if digits[0] == '?':
        product = 1
        for factor in digits[1:]:
            product *= int(factor)
        digits[0] = product
    digits = [int(d) for d in digits]
    return (digits[0], digits[1:])


def parse_prime_factor_string_something_missing(s: str) -> tuple[int, list[int]]:
    words: list[str] = s.split(' ')
    cleaned = [w.strip(' ,') for w in words]
    digits = [w for w in cleaned if (w.isdigit() or w == '?')]
    if digits[0] == '?':
        product = 1
        for factor in digits[1:]:
            product *= int(factor)
        digits[0] = product
    else:
        product = 1
        unknown_idx = 0
        for idx, factor in enumerate(digits[1:]):
            if factor == '?':
                unknown_idx = idx
            else:
                product *= int(factor)
        digits[unknown_idx + 1] = int(digits[0]) // product
    digits = [int(d) for d in digits]
    return (digits[0], digits[1:])


if __name__ == '__main__':
    assert parse_prime_factor_string("The prime factors of 16 are 2, 2, 2, 2") == (16, [2, 2, 2, 2])
    assert parse_prime_factor_string("The prime factors of 12 are 2, 2, 3") == (12, [2, 2, 3])
    assert parse_prime_factor_string("The prime factor of 227 is 227") == (227, [227])
    assert parse_prime_factor_string("The prime factors of 154 are 2, 7, 11") == (154, [2, 7, 11])

    assert parse_prime_factor_string_product_missing("The prime factors of 16 are 2, 2, 2, 2") == (16, [2, 2, 2, 2])
    assert parse_prime_factor_string_product_missing("The prime factors of ? are 2, 2, 3") == (12, [2, 2, 3])
    assert parse_prime_factor_string_product_missing("The prime factor of 227 is 227") == (227, [227])
    assert parse_prime_factor_string_product_missing("The prime factors of ? are 2, 7, 11") == (154, [2, 7, 11])

    assert parse_prime_factor_string_something_missing("The prime factors of 16 are 2, ?, 2, 2") == (16, [2, 2, 2, 2])
    assert parse_prime_factor_string_something_missing("The prime factors of 12 are 2, 2, ?") == (12, [2, 2, 3])
    assert parse_prime_factor_string_something_missing("The prime factor of 227 is ?") == (227, [227])
    assert parse_prime_factor_string_something_missing("The prime factors of ? are 2, 7, 11") == (154, [2, 7, 11])