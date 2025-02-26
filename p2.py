# Initialize an empty list to store the numbers
numbers = []

# Prompt user for input
while True:
    user_input = input("Enter a number (or type 'done' to finish): ")
    
    if user_input.lower() == 'done':
        break  # Exit the loop when 'done' is entered
    else:
        try:
            # Convert input to a float and add to the list
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

# Check if the list is not empty
if numbers:
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"The maximum number is: {max_num}")
    print(f"The minimum number is: {min_num}")
else:
    print("No numbers were entered.")
