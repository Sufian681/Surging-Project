def remove_rightmost_bit(n):
    return n & (n - 1)

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def is_power_of_four(n):
    return is_power_of_two(n) and (n & 0x55555555) != 0

def is_power_of_eight(n):
    return is_power_of_two(n) and (n & 0x24924924) != 0

def power_by_squaring(base, exp):
    result = 1
    while exp > 0:
        if exp & 1:
            result *= base
        base *= base
        exp >>= 1
    return result

print(f"Remove rightmost bit of 12 (1100): {remove_rightmost_bit(12)}")
print(f"Is 16 a power of 2, 4, 8? {is_power_of_two(16)}, {is_power_of_four(16)}, {is_power_of_eight(16)}")
print(f"2 raised to power 10: {power_by_squaring(2, 10)}")
print(f"Remove rightmost bit of 12 (1100): {remove_rightmost_bit(12)}")
print(f"Is 16 a power of 2, 4, 8? {is_power_of_two(16)}, {is_power_of_four(16)}, {is_power_of_eight(16)}")
print(f"2 raised to power 10: {power_by_squaring(2, 10)}")