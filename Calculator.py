def calculator():
  while True:
    # Get the user input
    user_input = input("Enter an arithmetic operation (+, -, *, /): ")

    # Check if the user wants to exit the calculator
    if user_input == "q":
      break

    # Get the operands
    num1 = float(input("Enter the first Number: "))
    num2 = float(input("Enter the second Number: "))

    # Perform the operation
    if user_input == "+":
      result = num1 + num2
    elif user_input == "-":
      result = num1 - num2
    elif user_input == "*":
      result = num1 * num2
    elif user_input == "/":
      result = num1 / num2
    else:
      result = "Invalid operator"

    # Print the result
    print(result)

# Run the calculator
calculator()
