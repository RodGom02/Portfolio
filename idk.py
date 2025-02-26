total = 0
count = 0

while True:
    user_input = input("Enter an integer (or type 'done' to finish): ")
    if user_input.lower() == 'done':
        break

    try:
        number = int(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input")

average = total/count if count > 0 else 0

print("\nResults")
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average:.2f}")