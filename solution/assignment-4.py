def reverse_string(s):
    if len(s) == 0:  # Base case: if the string is empty
        return s
    else:
        return reverse_string(s[1:]) + s[0]  # Recursive case

# Example usage
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print(f"The reversed string is: {reversed_string}")

