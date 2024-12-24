def print_alphabet_pattern(n):
    # Loop through each row
    for i in range(1, n + 1):
        # Calculate the number of leading spaces
        spaces = ' ' * (n - i)

        # Generate the first half of the alphabet sequence (A to the ith letter)
        first_half = [chr(65 + j) for j in range(i)]

        # Generate the second half (reverse of the first half, excluding the middle letter)
        second_half = first_half[:-1][::-1]

        # Combine the first and second halves
        row = first_half + second_half

        # Print the row with leading spaces
        print(spaces + ' '.join(row))

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_alphabet_pattern(num_lines)

