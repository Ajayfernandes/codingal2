def reverse_bits(n):
    binary_str = bin(n)[2:]

    reversed_str = binary_str[::-1]

    reversed_num = int(reversed_str, 2)
    return reversed_num

n = int(input("Enter a number: "))
result = reverse_bits(n)
print(f"Reversed bits result: {result}")