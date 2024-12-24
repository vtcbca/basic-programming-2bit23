def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:  # If characters don't match
            return False
        left += 1
        right -= 1
    return True

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

