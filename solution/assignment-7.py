def print_number_triangle(n):
    for i in range(1, n + 1):
        # Calculate leading spaces for centering the pattern
        spaces = ' ' * (n - i)

        # Create the number sequence for the row
        numbers = ' '.join(str(x) for x in range(1, 2 * i))

        # Print the row with spaces for centering
        print(spaces + numbers)

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_number_triangle(num_lines)

