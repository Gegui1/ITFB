def power_numbers(*args):
    return [x**2 for x in args]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_numbers(numbers, filter_type):
    if filter_type == ODD:
        return list(filter(lambda x: x % 2 != 0, numbers))
    elif filter_type == EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif filter_type == PRIME:
        return list(filter(is_prime, numbers))
    else:
        raise ValueError("Invalid filter type")


print(power_numbers(1, 2, 5, 7))

numbers = [1, 2, 3, 4, 5]
print(filter_numbers(numbers, ODD))
print(filter_numbers(numbers, EVEN))
print(filter_numbers(numbers, PRIME))

