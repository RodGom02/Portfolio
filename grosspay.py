try:
    # Get user input
    hours = int(input("Enter the number of hours: "))  
    pay = float(input("Enter the hourly pay rate: "))  

    # Calculate gross pay with overtime
    if hours > 40:
        gross_pay = (40 * pay) + ((hours - 40) * (pay * 1.5))  # Overtime pay
    else:
        gross_pay = hours * pay  

    # Calculate yearly pay
    yearly_pay = gross_pay * 52  

    # Display results
    print(f"The gross pay is ${gross_pay:.2f}")
    print(f"The yearly pay is ${yearly_pay:.2f}")

except ValueError:  # Catch non-numeric input errors
    print("Error: Please enter numeric values for hours and pay rate.")
