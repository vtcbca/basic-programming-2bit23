def print_star_pattern(n):
    for i in range(1, n + 1):
        # Inner loop to print stars in each row
        for j in range(i):
            print("*", end=" ")  # Print star without a new line
        
        # Move to the next line after printing all stars for this row
        print()

# Example usage
num_lines = int(input("Enter the number of lines: "))
print_star_pattern(num_lines)

