def fibonacci_max_value(max_value):
    fib_sequence = []
    a, b = 0, 1  # Starting values of the Fibonacci sequence
    while a < max_value:
        fib_sequence.append(a)
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    return fib_sequence

# Example usage
max_value = int(input("Enter the maximum value: "))
sequence = fibonacci_max_value(max_value)
print(f"The Fibonacci sequence less than {max_value} is: {sequence}")

