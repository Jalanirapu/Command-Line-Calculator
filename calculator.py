# --- Simple Command-Line Calculator in Python ---

def main():
    """
    The main function to run the calculator loop.
    """
    print("Welcome to the Simple Calculator!")
    print("You can add (+), subtract (-), multiply (*), and divide (/).")
    print("-" * 30)

    # This loop will continue forever until the user decides to exit
    while True:
        # 1. GET USER INPUT
        try:
            num1_str = input("Enter the first number: ")
            # Allow user to type 'exit' to quit
            if num1_str.lower() == 'exit':
                break
            num1 = float(num1_str)

            operator = input("Enter an operator (+, -, *, /): ")
            
            num2_str = input("Enter the second number: ")
            # Allow user to type 'exit' to quit
            if num2_str.lower() == 'exit':
                break
            num2 = float(num2_str)

        except ValueError:
            # This block runs if float() fails because the input was not a number
            print("Invalid input. Please enter valid numbers. Try again.")
            print("-" * 30)
            continue # Skip the rest of this loop and start a new one

        # 2. PERFORM CALCULATION
        # We use a variable 'result' to store the outcome. Initialize to None.
        result = None
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Check for division by zero, a common and critical error
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
        else:
            # Handle cases where the operator is not one of the valid ones
            print("Error: Invalid operator. Please use +, -, *, or /.")

        # 3. DISPLAY THE RESULT
        # Only print the result if a calculation was successfully performed
        if result is not None:
            print(f"Result: {num1} {operator} {num2} = {result}")

        print("-" * 30)

        # 4. ASK TO CONTINUE
        # We check if the user wants to do another calculation.
        # .lower() makes the check case-insensitive (so 'YES' or 'Yes' also work)
        another = input("Do another calculation? (yes/no): ")
        if another.lower() != 'yes':
            break # Exit the while loop

    # This line runs only after the loop has been broken
    print("Thank you for using the calculator. Goodbye!")

# This standard Python construct ensures that main() is called only when the script is executed directly
if __name__ == "__main__":
    main()